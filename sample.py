import random

# 出す手の種類データ
hands = ['グー','チョキ','パー']

# じゃんけんの判定を持つデータ
judge = ['あいこ','かち','まけ']

win = 0 # 勝利数を数える値
draw = 0 # 引き分け数を数える値
count = 0 # 勝負数を数える値


# ゲーム開始
print('=== じゃんけんをしましょう！ ===')
print('ルール : 入力できる値は 0:グー, 1:チョキ, 2:パー')
print('じゃんけん....')

# player
player = int(input('>>>>'))

while count < 3:

    if player == 0 or player == 1 or player == 2 :
        print('あなた:' + hands[player])

        #あいての実装
        # やっていること
        # ランダムで０〜２の数字を出力するようにかいている
        computer = random.randint(0,2)

        # ここであいての手の内容を出力
        print('コンピュータ：' + hands[computer])

        #勝敗（0:あいこ / 1:プレイヤの負け / 2:プレイヤの勝ち）
        decision = (player - computer + 3) % 3

        if decision == 0:
            draw += 1
        elif decision == 2:
            win += 1

        #結果の表示
        print("『" + judge[decision]+"』\n")

        count += 1

    else:
        #入力エラー
        print('0～2を数値入力してください')

    #3回勝負の結果
print("===========================")
print('3回勝負の結果は' + str(win) + "勝" + str(draw) + "分けです")
print("===========================\n")