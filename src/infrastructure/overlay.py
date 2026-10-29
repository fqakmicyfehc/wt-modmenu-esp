"""GLFW + ImGui transparent overlay window."""
from __future__ import annotations

import glfw
from imgui.integrations.glfw import GlfwRenderer
import imgui

from ..host.registry import FeatureRegistry


class OverlayWindow:
    def __init__(self, registry: FeatureRegistry, title: str = "ModMenu") -> None:
        self.registry = registry
        self.title = title

    def _init(self) -> None:
        if not glfw.init():
            raise RuntimeError("glfw.init failed")
        glfw.window_hint(glfw.TRANSPARENT_FRAMEBUFFER, True)
        glfw.window_hint(glfw.FLOATING, True)
        self.window = glfw.create_window(1920, 1080, self.title, None, None)
        glfw.make_context_current(self.window)
        imgui.create_context()
        self.impl = GlfwRenderer(self.window)

    def run(self) -> None:
        self._init()
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            self.impl.process_inputs()
            imgui.new_frame()
            for feat in self.registry.all():
                if feat.draw:
                    feat.draw(self)
            imgui.render()
            self.impl.render(imgui.get_draw_data())
            glfw.swap_buffers(self.window)
        self.impl.shutdown()
        glfw.terminate()