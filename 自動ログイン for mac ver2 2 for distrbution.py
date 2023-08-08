import webbrowser
import pyautogui
import time


# Autmatic google log in


# # time.sleep(10)#この場合実行後２秒に止めた場所のマウス位置を表す
# for i in range(1,100000):
#     print(pyautogui.position())#クリックしたい位置の座標を確認


# ID,Passをリストで入力
# [google ID, password]の順番で自分が理解できる変数名にしてIDとパスを格納
yamafuji = ['yamafuji2', 'yourpassword1']
ppp = ['ppp','yourpassword2']


# 大枠のからのリスト作成
id_pass=[]
# ID,Passの変数をextendの中に入れて更にリスト化
id_pass.extend([yamafuji,ppp])


# キーを押し続ける#オンにするとログインできない＋
    # macで使うにあたって、設定⇨キーボード⇨入力ソースの中の「Caps Lockの動作」を「オンの時「英字」を入力」の設定をする offにした
# pyautogui.keyDown('capslock')


# lenでid_passに入った合計を取り、range()で１個ずつ取れるようにする
for i in range(len(id_pass)):
    # gooleのログインページのURL
    google_login_url = "https://accounts.google.com/signin/v2/identifier?hl=ja&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession"
    #chromeを開くorタブの追加
    webbrowser.open(google_login_url)#仮にクローム開いていればこのタブが追加される
    time.sleep(4)
    # id_passの中に入れた各リストのIDを入力
    pyautogui.typewrite(id_pass[i][0])
    # エンター押してパスワード入力画面へ
    pyautogui.press('enter')
    time.sleep(5)
    # id_passの中に入れた各リストのパスワードを入力
    pyautogui.typewrite(id_pass[i][1])
    #  エンター押してログインする
    pyautogui.press('return')

