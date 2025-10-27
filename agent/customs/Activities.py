from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.custom_recognition import RecognitionResult
from maa.context import Context

import time

from .GridScheduling import HexagonGridManager
from .utils import Prompt, Tasker, RecoHelper, parse_query_args, PresetLoader


gear = 1


@AgentServer.custom_action("set_operate_gear")
class SetOperateGear(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        global gear
        try:
            args = parse_query_args(argv)
            gear_level = args.get("g", "m")
            if gear_level == "f":
                gear = 0.5
            elif gear_level == "s":
                gear = 2
            else:
                gear = 1
            Prompt.log(f"设置操作间隔为 {gear} 倍速")
            return True
        except Exception as e:
            return Prompt.error("设置操作间隔", e)


@AgentServer.custom_action("shxq")
class AutoSearch(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        global gear
        try:
            levels = PresetLoader.read("shxq")
            while True:
                if Tasker.is_stopping(context):
                    return False

                # 识别关卡
                level = (
                    RecoHelper(context)
                    .recognize("十环线圈_识别关卡")
                    .reco_detail.best_result.text
                )

                # 普通模式
                ops = levels.get(level, None)
                if not ops:
                    return Prompt.error("十环线圈", "未定义的关卡")
                Prompt.log(f"当前关卡：{level}")

                # 执行点击
                hg = HexagonGridManager.get()
                for op in ops:
                    if Tasker.is_stopping(context):
                        return False
                    Prompt.log(f"充能线圈：[{op[0]}, {op[1]}]")
                    Tasker.click(context, *hg.get_point(op[0], op[1]))
                    interval = 0.2 if len(op) < 3 else op[2]
                    time.sleep(gear * interval)

                # 进入下一关
                wt = 0
                while True:
                    if Tasker.is_stopping(context):
                        return False
                    if RecoHelper(context).recognize("十环线圈_关卡完成").hit():
                        if level == "第15关":
                            return True
                        time.sleep(0.4 * gear)
                        Prompt.log(f"关卡完成，即将进入下一关！")
                        Tasker.click(context, 639, 526)
                        time.sleep(gear)
                        break
                    wt += 1
                    if wt > 12 * gear:
                        return Prompt.error("十环线圈", "关卡失败！")
                    time.sleep(gear)

        except Exception as e:
            return Prompt.error("十环线圈", e)
