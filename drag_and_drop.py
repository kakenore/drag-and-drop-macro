import pyautogui
import time
import keyboard

def drag_and_drop(start_x, start_y, end_x, end_y, duration=0.05):
    pyautogui.moveTo(start_x, start_y, duration=0.1)  # マウスが最初の位置に戻る速度を早くする
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.moveTo(end_x, end_y, duration=duration)
    pyautogui.mouseUp()

# エスケープキーを押したらループを終了する
def on_escape_pressed(e):
    if e.name == 'esc':
        global running
        running = False

# エスケープキーのリスナーを登録
keyboard.on_press(on_escape_pressed)

running = True
repeat_count = 129

print("スペースキーを押してください。")
keyboard.wait("space")
start_x, start_y = pyautogui.position()

print("スペースキーを再度押してください。")
keyboard.wait("space")
end_x, end_y = pyautogui.position()

while running and repeat_count > 0:
    drag_and_drop(start_x, start_y, end_x, end_y)
    time.sleep(0.05)  # ドラッグアンドドロップの間隔を設  定（必要に応じて調整）
    repeat_count -= 1

print("プログラムを終了します。")
  