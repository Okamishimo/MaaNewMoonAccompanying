from maa.custom_action import CustomAction
from maa.custom_recognition import CustomRecognition, RecognitionResult, RectType
from maa.context import Context
from maa.controller import Controller

from typing import Dict, Any
import os
import json
import re
import time
import numpy as np
from openai import OpenAI


# 间隔输出
def cprint(*args, **kwargs):
    time.sleep(0.05)
    print(*args, **kwargs)
    time.sleep(0.05)


# 解析查询字符串
def parse_query_args(argv: CustomAction.RunArg) -> dict[str, Any]:
    if not argv.custom_action_param:
        return {}

    # 预处理参数：去除首尾引号并按'&'分割参数列表
    args: list[str] = argv.custom_action_param.strip("\"'").split("&")

    # 解析键值对到字典
    params: Dict[str, Any] = {}
    for arg in args:
        # 分割键值
        parts = arg.split("=")
        if len(parts) >= 2:
            params[parts[0]] = parts[1]

    return params


# 解析列表输入
def parse_list_input(input: str, split_regex=r",\s*|，\s*|、\s*|\s+") -> list[str]:
    if not input:
        return []

    items = re.split(split_regex, input)
    items = [item for item in items if item]

    return items


# 提示
class Prompt:
    @staticmethod
    def log(
        content: str = "",
        is_continuous=False,
        use_default_prefix=True,
        use_pre_devider=False,
        use_post_devider=False,
    ):
        if use_default_prefix and not (use_pre_devider or use_post_devider):
            content = f"> {content}"
        if use_pre_devider:
            cprint("——" * 5)
        cprint(content) if is_continuous else print(content)
        if use_post_devider:
            cprint("——" * 5)

    @staticmethod
    def error(
        content: str,
        e: Exception = None,
        reco_detail: str = None,
        use_defult_postfix=True,
    ):
        if use_defult_postfix:
            content += "失败，请立即停止运行程序！"
        cprint("——" * 5)
        cprint(f"{content}")
        if e is not None:
            cprint("错误详情：")
            cprint(e)
        cprint("——" * 5)
        return (
            False
            if reco_detail == None
            else CustomRecognition.AnalyzeResult(
                box=None, detail="程序错误" if reco_detail == True else reco_detail
            )
        )


# 本地存储
class LocalStorage:
    # 存储文件路径
    agent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_dir = os.path.join(agent_dir, "..", "config")
    storage_path = os.path.join(config_dir, "mnma_storage.json")

    # 检查并确保存储文件存在
    @classmethod
    def ensure_storage_file(cls):
        # 确保配置目录存在
        if not os.path.exists(cls.config_dir):
            os.makedirs(cls.config_dir)

        # 确保存储文件存在
        if not os.path.exists(cls.storage_path):
            with open(cls.storage_path, "w", encoding="utf-8") as f:
                json.dump({}, f)

    # 读取存储数据
    @classmethod
    def read(cls) -> dict:
        cls.ensure_storage_file()
        try:
            with open(cls.storage_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # 存储文件格式错误时重置为空对象
            with open(cls.storage_path, "w", encoding="utf-8") as f:
                json.dump({}, f)
            return {}

    # 获取存储值
    @classmethod
    def get(cls, task: str, key: str) -> str | bool | int | None:
        storage = cls.read()
        task_storage = storage.get(task)
        if task_storage is None:
            return None
        return task_storage.get(key)

    # 写入存储数据到文件
    @classmethod
    def write(cls, storage: dict) -> bool:
        try:
            with open(cls.storage_path, "w", encoding="utf-8") as f:
                json.dump(storage, f)
            return True
        except Exception as e:
            print(f"存储数据时出错: {e}")
            return False

    # 设置存储值
    @classmethod
    def set(cls, task: str, key: str, value: str | bool | int) -> bool:
        storage = cls.read()
        if task not in storage:
            storage[task] = {}
        storage[task][key] = value

        return cls.write(storage)


# 预制数据
class PresetLoader:
    # 文件夹路径
    agent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    presets_dir = os.path.join(agent_dir, "presets")

    # 读取
    @classmethod
    def read(cls, filename: str) -> dict:
        try:
            if not filename.endswith(".jsonc"):
                filename += ".jsonc"
            with open(
                os.path.join(cls.presets_dir, filename), "r", encoding="utf-8"
            ) as f:
                return json.load(f)
        except json.JSONDecodeError:
            raise ValueError("数据文件丢失！")


# 全局设置
class Configs:
    configs = {}

    @classmethod
    def set(cls, key: str, value: str):
        # 转义类型
        if value == "true":
            value = True
        elif value == "false":
            value = False
        elif value.isdigit():
            value = int(value)

        cls.configs[key] = value

    @classmethod
    def get(cls, key: str, default=None) -> str | bool | int | None:
        if (key not in cls.configs) and (default is not None):
            cls.configs[key] = default
        return cls.configs.get(key, default)


# 控制器
class Tasker:
    # 获取控制器
    @staticmethod
    def _ctrler(context: Context):
        return context.tasker.controller

    # 运行单个节点
    @staticmethod
    def run_node(context: Context, node: str):
        context.run_task(node, {node: {"next": [], "interrupt": [], "on_error": []}})

    # 是否正在停止
    @staticmethod
    def is_stopping(context: Context):
        return context.tasker.stopping

    # 截图
    @staticmethod
    def screenshot(context: Context) -> np.ndarray:
        return Tasker._ctrler(context).post_screencap().wait().get()

    # 点击
    @staticmethod
    def click(context: Context, x: int, y: int):
        return Tasker._ctrler(context).post_click(x, y).wait()


# 识别器
class RecoHelper:
    NoResult = CustomRecognition.AnalyzeResult(box=None, detail="无目标")

    def __init__(self, context: Context, argv: CustomRecognition.AnalyzeArg = None):
        self.context = context
        self.argv = argv
        self.screencap: np.ndarray | None = None

    def refresh_screencap(self, context=None) -> np.ndarray:
        if context:
            self.context = context
        self.screencap = Tasker.screenshot(self.context)
        return self.screencap

    # 识别结果
    def recognize(
        self, node: str = "识别", override_key_value: dict = {}, refresh_image=False
    ):
        if refresh_image:
            image = self.refresh_screencap()
        elif self.screencap is not None:
            image = self.screencap
        elif self.argv:
            image = self.argv.image
        else:
            image = self.refresh_screencap()
        self.reco_detail = self.context.run_recognition(
            node, image, {node: override_key_value}
        )
        return self

    # 是否识别到结果
    def hit(self):
        return self.reco_detail is not None

    # 点击
    def click(
        self, context: Context = None, offset: tuple[int, int] = (0, 0)
    ) -> tuple[int, int] | None:
        if not self.hit():
            return None
        res = self.reco_detail.best_result
        target = RecoHelper.get_res_center(res)
        target = (target[0] + offset[0], target[1] + offset[1])
        if context is None:
            context = self.context
        Tasker.click(context, *target)
        return target

    def click_all(
        self,
        context: Context = None,
        offset: tuple[int, int] = (0, 0),
        interval=0.2,
        max_num=99999,
    ) -> tuple[int, int] | None:
        if not self.hit():
            return None
        results = self.reco_detail.filterd_results
        targets = []
        for i, res in enumerate(results):
            if i + 1 > max_num:
                break
            if i > 0:
                time.sleep(interval)
            target = RecoHelper.get_res_center(res)
            target = (target[0] + offset[0], target[1] + offset[1])
            targets.append(target)
            if context is None:
                context = self.context
            Tasker.click(context, *target)
        return targets

    # 结果拼接
    def concat(self) -> str:
        if not self.hit():
            return None
        results = self.reco_detail.filterd_results
        text = ""
        for res in results:
            text += res.text
        return text

    # 计算识别结果中心坐标
    @staticmethod
    def get_res_center(result: RecognitionResult) -> tuple[int, int]:
        box = result.box
        return (round(box[0] + box[2] / 2), round(box[1] + box[3] / 2))

    # 统一可信度过滤
    @staticmethod
    def filter_reco(results: list[RecognitionResult], threshold: float = 0.7):
        return [r for r in results if r.score >= threshold]

    # 排序
    @staticmethod
    def sort_reco(results: list[RecognitionResult]):
        return sorted(results, key=lambda r: r.score, reverse=True)

    # 返回结果
    @staticmethod
    def rt(box: RectType = (1, 1, 1, 1), text: str = ""):
        return CustomRecognition.AnalyzeResult(box, text)


# 判断器
class Judge:
    @staticmethod
    def equal_process(
        context: Context,
        analyze_arg: CustomRecognition.AnalyzeArg,
        carrier_node: str,
        split_key="/",
        return_analyze_result=False,
    ) -> CustomRecognition.AnalyzeResult | bool:
        reco_detail = context.run_recognition(carrier_node, analyze_arg.image)
        for res in reco_detail.all_results:
            scores = res.text.split(split_key)
            if len(scores) == 2:
                if scores[0] == scores[1]:
                    return (
                        CustomRecognition.AnalyzeResult(
                            box=res.box,
                            detail=res.text,
                        )
                        if return_analyze_result
                        else True
                    )
        return (
            CustomRecognition.AnalyzeResult(box=None, detail="无目标")
            if return_analyze_result
            else False
        )

    @staticmethod
    # 精准数值匹配
    def exact_number(text: str, target_value: str) -> bool:
        # 整数
        int_pattern = r"(?<!\d|\.)" + re.escape(target_value) + r"(?!\d|\.)"
        # 小数
        decimal_pattern = r"(?<!\d|\.)" + re.escape(target_value) + r"\.0+(?!\d)"
        # 检测
        pattern = f"({int_pattern}|{decimal_pattern})"
        return bool(re.search(pattern, text))


# AI 接口
class ChatHolder:
    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str,
        ans_require="",
        ans_limit="你是新月同行游戏小助手，使用中文回答用户问题。",
    ):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )
        self.model = model
        self.messages = [{"role": "system", "content": f"{ans_require}\n{ans_limit}"}]

    # 对话
    def answer(
        self, qas: str, thinking=True, rt_thinking=False
    ) -> str | tuple[str, str]:
        # 构造请求体
        self.messages.append({"role": "user", "content": qas})
        body = {
            "model": self.model,
            "messages": self.messages,
            "stream": True,
        }
        if thinking:
            body["extra_body"] = {"enable_thinking": True}

        # 发送请求
        reason = ""
        content = ""
        for chunk in self.client.chat.completions.create(**body):
            try:
                choice = chunk.choices[0]
                delta = getattr(choice, "delta", None)
                if delta is None:
                    continue
                rc = getattr(delta, "reasoning_content", None)
                if rc:
                    reason += rc
                ct = getattr(delta, "content", None)
                if ct:
                    content += ct
            except Exception:
                continue

        # 保存记录
        self.messages.append({"role": "assistant", "content": content})

        if rt_thinking:
            return reason, content
        return content
