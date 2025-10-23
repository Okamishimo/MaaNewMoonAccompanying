from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context

from .utils import parse_query_args, Prompt, RecoHelper


check_quick_event = False


# 初始化城市事件
@AgentServer.custom_action("init_city_walk")
class InitCityWalk(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        global check_quick_event
        try:
            check_quick_event = False
            return True
        except Exception as e:
            return Prompt.error("初始化城市事件", e)


# 检查快速事件
@AgentServer.custom_action("check_quick_event")
class CheckQuickEvent(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        global check_quick_event
        try:
            return not check_quick_event
        except Exception as e:
            return Prompt.error("检查快速事件", e)


# 记录快速事件
@AgentServer.custom_action("record_quick_event")
class RecordQuickEvent(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        global check_quick_event
        try:
            check_quick_event = True
            return True
        except Exception as e:
            return Prompt.error("记录快速事件", e)


# 指定作战队伍
@AgentServer.custom_action("set_event_squad")
class SetEventSquad(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        try:
            args = parse_query_args(argv)
            squad = args.get("s", "")

            if squad != "":
                print(f"> 行动将使用队伍：{squad}")
            else:
                context.override_pipeline(
                    {
                        "城市探索_进入战斗": {"next": "城市探索_开始战斗"},
                    }
                )

            return True
        except Exception as e:
            return Prompt.error("设定指定队伍", e)


target_first = False


# 强制指定项优先
@AgentServer.custom_action("set_delegation_config")
class SetDelegationConfig(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        global target_first
        try:
            args = parse_query_args(argv)
            target_first = True if args.get("value", "false") == "true" else False
            return True
        except Exception as e:
            return Prompt.error("设置指定项强制优先", e)


# 处理委托
@AgentServer.custom_action("handle_delegation")
class HandleDelegation(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        global target_first
        try:
            args = parse_query_args(argv)
            target = args.get("target", "整流元件")

            target_rh = RecoHelper(context).recognize(
                "城市探索_委托项", {"expected": target}
            )
            if target_first:
                Prompt.log("直接选择指定项")
                target_rh.click()
            else:
                target_y = target_rh.reco_detail.best_result.box[1]
                high_rh = RecoHelper(context).recognize(
                    "城市探索_委托项", {"expected": "高风险高收益"}
                )
                flag = True
                for result in high_rh.reco_detail.filterd_results:
                    if abs(target_y - result.box[1]) < 45:
                        Prompt.log("选择高收益指定项")
                        target_rh.click()
                        flag = False
                        break
                if flag:
                    Prompt.log("指定项非高收益，选择其他项")
                    high_rh.click()

            return True
        except Exception as e:
            return Prompt.error("处理委托", e)
