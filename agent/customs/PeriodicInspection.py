from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context

from typing import Optional
from datetime import datetime, date, timedelta

from .utils import parse_query_args, LocalStorage, Prompt

# 全局刷新时间配置
REFRESH_HOUR = 4


class Inspector:
    @staticmethod
    def _adjust_datetime(refresh_hour: int = REFRESH_HOUR) -> datetime:
        """
        根据刷新时间调整日期
        如果当前时间小于刷新时间，则认为是前一天
        """
        current_datetime = datetime.now()
        if current_datetime.hour < refresh_hour:
            return current_datetime - timedelta(days=1)
        return current_datetime

    # 记录检查
    @staticmethod
    def record(task: str, refresh_hour: int = REFRESH_HOUR) -> None:
        """
        记录任务的最后日期，根据刷新时间调整日期
        """
        current_datetime = Inspector._adjust_datetime(refresh_hour)
        LocalStorage.set(task, "last_date", str(current_datetime.date()))

    # 是否在同一周
    @staticmethod
    def same_week(task: str, refresh_hour: int = REFRESH_HOUR) -> bool:
        current_datetime = Inspector._adjust_datetime(refresh_hour)
        last_date_str: Optional[str] = LocalStorage.get(task, "last_date")

        if not last_date_str:
            return False

        try:
            last_date = date.fromisoformat(last_date_str)
        except Exception as e:
            return False

        return (
            current_datetime.isocalendar()[1] == last_date.isocalendar()[1]
            and current_datetime.year == last_date.year
        )

    # 是否在同一天
    @staticmethod
    def same_day(task: str, refresh_hour: int = REFRESH_HOUR) -> bool:
        current_datetime = Inspector._adjust_datetime(refresh_hour)
        last_date_str: Optional[str] = LocalStorage.get(task, "last_date")

        if not last_date_str:
            return False

        try:
            last_date = date.fromisoformat(last_date_str)
        except (ValueError, TypeError):
            return False

        return current_datetime.date() == last_date


# 周期检查
@AgentServer.custom_action("periodic_check")
class PeriodicCheck(CustomAction):
    """
    在当天或本周时，节点返回error，即仅在没有指定记录时通过节点，在有记录时走上一个节点的on_error路径
    """

    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        try:
            args = parse_query_args(argv)
            task = args.get("t")
            periodic = args.get("p", "day")
            record_immediately = args.get("r", False)
            if record_immediately == "true":
                record_immediately = True
            else:
                record_immediately = False

            flag = False
            if periodic == "week":
                flag = Inspector.same_week(task)
            elif periodic == "day":
                flag = Inspector.same_day(task)

            if record_immediately:
                Inspector.record(task)

            return not flag
        except Exception as e:
            return Prompt.error("检查周期任务", e)


# 记录检查
@AgentServer.custom_action("record_period")
class SetLastPeriodicCheck(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        try:
            args = parse_query_args(argv)
            task = args.get("t")
            Inspector.record(task)
            return True
        except Exception as e:
            return Prompt.error("记录检查时间", e)
