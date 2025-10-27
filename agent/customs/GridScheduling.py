from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context

import math

from .utils import parse_query_args, Prompt, Tasker


# 矩阵操作


class StepMatrix:
    def __init__(self, origin: tuple, step_size: tuple):
        self.origin = origin
        self.step_size = step_size

    def get_point(self, row: int = 1, col: int = 1) -> tuple:
        return (
            self.origin[0] + self.step_size[0] * (col - 1),
            self.origin[1] + self.step_size[1] * (row - 1),
        )

    def click(self, context: Context, row: int = 1, col: int = 1) -> bool:
        target = self.get_point(row, col)
        Tasker.click(context, *target)


class StepMatrixManager:
    step_matrixes = {}

    @classmethod
    def init(cls, origin: tuple, step_size: tuple, key="default"):
        cls.step_matrixes[key] = StepMatrix(origin, step_size)
        return cls.step_matrixes[key]

    @classmethod
    def get(cls, key="default") -> StepMatrix:
        return cls.step_matrixes[key]


# 初始化矩阵
@AgentServer.custom_action("init_step_matrix")
class InitStepMatrix(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        try:
            args = parse_query_args(argv)
            origin = (int(args.get("ox")), int(args.get("oy")))
            step_size = (int(args.get("sx")), int(args.get("sy")))

            StepMatrixManager.init(origin, step_size)

            return True

        except Exception as e:
            return Prompt.error("初始化步长矩阵", e)


# 六边形网格
class HexagonGrid:
    def __init__(self, origin: tuple[int, int], gap: int, width: int):
        self.origin = (origin[0] - gap, origin[1])
        self.gap = gap
        self.width = width

    def get_point(self, l=0, c=0) -> tuple[int, int]:
        if c < 0:
            c = self.width - abs(l) + c + 1
        elif c == 0:
            c = 1
        ox = self.gap / 2 * -l
        x = self.origin[0] + abs(ox) + c * self.gap
        y = self.origin[1] + ox * math.sqrt(3)
        return (int(round(x)), int(round(y)))


class HexagonGridManager:
    hexagon_grids = {}

    @classmethod
    def init(cls, origin: tuple[int, int], gap: int, width: int, key="default"):
        cls.hexagon_grids[key] = HexagonGrid(origin, gap, width)
        return cls.hexagon_grids[key]

    @classmethod
    def get(cls, key="default") -> HexagonGrid:
        return cls.hexagon_grids[key]


# 初始化六边形网格
@AgentServer.custom_action("init_hexagon_grid")
class InitHexagonGrid(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        try:
            args = parse_query_args(argv)
            origin = (int(args.get("ox")), int(args.get("oy")))
            gap = int(args.get("gap"))
            width = int(args.get("w"))
            HexagonGridManager.init(origin, gap, width)
            return True
        except Exception as e:
            return Prompt.error("初始化六边形网格", e)
