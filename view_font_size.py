import sublime
import sublime_plugin


class IncreaseViewFontSizeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        current = self.view.settings().get("font_size", 10)

        if current >= 36:
            current += 4
        elif current >= 24:
            current += 2
        else:
            current += 1

        if current > 128:
            current = 128
        self.view.settings().set("font_size", current)


class DecreaseViewFontSizeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        current = self.view.settings().get("font_size", 10)
        # current -= 1

        if current >= 40:
            current -= 4
        elif current >= 26:
            current -= 2
        else:
            current -= 1

        if current < 8:
            current = 8
        self.view.settings().set("font_size", current)
