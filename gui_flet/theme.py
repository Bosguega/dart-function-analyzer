import flet as ft

# Cores do tema
class ThemeColors:
    PRIMARY = ft.Colors.BLUE_600
    SECONDARY = ft.Colors.BLUE_400
    SUCCESS = ft.Colors.GREEN_600
    ERROR = ft.Colors.RED_600
    WARNING = ft.Colors.ORANGE_600
    BACKGROUND = ft.Colors.WHITE
    SURFACE = ft.Colors.GREY_50
    TEXT_PRIMARY = ft.Colors.GREY_900
    TEXT_SECONDARY = ft.Colors.GREY_600
    TEXT_DISABLED = ft.Colors.GREY_400

# Estilos de texto
class TextStyles:
    TITLE = ft.TextStyle(
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ThemeColors.PRIMARY
    )
    
    SUBTITLE = ft.TextStyle(
        size=16,
        color=ThemeColors.TEXT_SECONDARY
    )
    
    SECTION_TITLE = ft.TextStyle(
        size=18,
        weight=ft.FontWeight.BOLD,
        color=ThemeColors.TEXT_PRIMARY
    )
    
    BODY = ft.TextStyle(
        size=14,
        color=ThemeColors.TEXT_PRIMARY
    )
    
    MONOSPACE = ft.TextStyle(
        font_family="monospace",
        size=12,
        color=ThemeColors.TEXT_PRIMARY
    )

# Estilos de botão
class ButtonStyles:
    PRIMARY = ft.ButtonStyle(
        bgcolor=ThemeColors.PRIMARY,
        color=ThemeColors.BACKGROUND,
        elevation=3
    )
    
    SECONDARY = ft.ButtonStyle(
        bgcolor=ThemeColors.SECONDARY,
        color=ThemeColors.BACKGROUND,
        elevation=2
    )
    
    SUCCESS = ft.ButtonStyle(
        bgcolor=ThemeColors.SUCCESS,
        color=ThemeColors.BACKGROUND,
        elevation=2
    )
    
    OUTLINED = ft.ButtonStyle(
        bgcolor=ThemeColors.BACKGROUND,
        color=ThemeColors.PRIMARY,
        side=ft.BorderSide(color=ThemeColors.PRIMARY, width=1)
    )

# Padding e margens
class Spacing:
    CARD_PADDING = ft.padding.all(20)
    CARD_MARGIN = ft.margin.only(bottom=20)
    HEADER_PADDING = ft.padding.only(top=20, bottom=30)
    FOOTER_PADDING = ft.padding.only(bottom=20)
    SECTION_SPACING = ft.margin.only(bottom=10)
    ELEMENT_SPACING = 10

# Configurações de componentes
class ComponentStyles:
    CARD = {
        "elevation": 2,
        "margin": Spacing.CARD_MARGIN,
        "color": ThemeColors.SURFACE
    }
    
    CONTAINER = {
        "padding": Spacing.CARD_PADDING
    }
    
    TEXT_FIELD = {
        "border_color": ThemeColors.TEXT_DISABLED,
        "focused_border_color": ThemeColors.PRIMARY,
        "text_style": TextStyles.BODY
    }
    
    DROPDOWN = {
        "border_color": ThemeColors.TEXT_DISABLED,
        "focused_border_color": ThemeColors.PRIMARY,
        "text_style": TextStyles.BODY
    }