from abc import ABC, abstractmethod
from typing import Any
from fastapi import UploadFile
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)


# Abstract Interface
class Pipeline(ABC):
    @abstractmethod
    def run_pipeline(self,
                     payload: str,
                     query_inputs: [str],
                     query_types: [str],
                     query: str,
                     file_path: str = None,
                     file: UploadFile = None,
                     debug: bool = False,
                     local: bool = True) -> Any:
        pass


# Factory Method
def get_pipeline(agent_name: str) -> Pipeline:
    if agent_name == "llamaindex":
        from .llamaindex import LlamaIndexPipeline
        return LlamaIndexPipeline()
    elif agent_name == "haystack":
        from .haystack import HaystackPipeline
        return HaystackPipeline()
    elif agent_name == "vllamaindex":
        from .vllamaindex import VLlamaIndexPipeline
        return VLlamaIndexPipeline()
    elif agent_name == "vprocessor":
        from .vprocessor import VProcessorPipeline
        return VProcessorPipeline()
    else:
        raise ValueError(f"Unknown agent: {agent_name}")

