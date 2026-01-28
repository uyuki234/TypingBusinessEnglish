"""ゲーム設定を管理するモジュール"""


class Config:
    """ゲーム設定を管理するクラス"""
    # ボタンの配置などを定義
    WIDTH = 1440
    HEIGHT = 640
    RIGHT_WIDTH = 480     # 右側の幅（固定）、左側は余った領域
    BG_COLOR = (24, 24, 32)
    TEXT_COLOR = (235, 235, 235)
    FPS = 60
    BTN_IMAGE_RATIO = 0.35
    PANEL_BG = (34, 34, 46)
    PANEL_RECT = (58, 92, 130)
    PANEL_RECT_BORDER = (120, 160, 200)
    PANEL_BTN = (80, 140, 200)
    PANEL_BTN_BORDER = (180, 210, 240)
    LEVEL_BAR_BG = (40, 40, 50)
    LEVEL_BAR_FILL = (90, 170, 120)
    LEVEL_BAR_BORDER = (180, 210, 240)
