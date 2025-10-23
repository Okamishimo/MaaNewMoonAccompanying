import time
from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context

from .utils import Tasker, parse_query_args, Prompt


# 选择编队
@AgentServer.custom_action("run_set_squad")
class RunSetSquad(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        try:
            args = parse_query_args(argv)
            expected = args.get("e", "")
            if expected == "":
                return False
            context.run_task(
                "选择编队_开始",
                {
                    "选择编队_检测当前编队": {"expected": expected},
                    "选择编队_找到指定编队": {"expected": expected},
                },
            )
            return True
        except Exception as e:
            return Prompt.error("选择编队", e)


# 进入活动面板
@AgentServer.custom_action("run_enter_activity")
class RunSetSquad(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        try:
            args = parse_query_args(argv)
            expected = args.get("title", "")
            if expected == "":
                return False
            context.run_task(
                "进入活动面板_开始",
                {"进入活动面板_识别到指定活动": {"expected": expected}},
            )
            return True
        except Exception as e:
            return Prompt.error("进入活动面板", e)


# 连续点击
@AgentServer.custom_action("click_many")
class ClickMany(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        try:
            args = parse_query_args(argv)
            times = args.get("t", "1")
            times = int(times)
            interval = args.get("i", "0.4")
            interval = float(interval)
            while times > 0:
                Tasker.click(context, 5, 5)
                time.sleep(interval)
                times -= 1
            return True
        except Exception as e:
            return Prompt.error("连续点击", e)
