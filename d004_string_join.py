# Dランクスキルチェック
# D004:文字列の結合で作成したコード
# 問題概要:
# 複数行で入力される文字列をカンマで一行に結合し
# 先頭に "Hello "(Hello + 半角スペース) を付け、
# 末尾に"."を付けて出力する。

# 入力例:
# 2
# Paiza
# Gino
# 
# 出力例
# Hello　Paiza,Gino.

n = int(input()) 			# 入力された文字列の数を受け取る
s_list = []	 			# 入力された文字列を格納するリスト

for _ in range(n): 			# 文字列の数だけ繰り返す
    s_list.append(input())　		# 入力された文字列をリストに追加
joined_names = ",".join(s_list)		# リスト内の文字列をカンマで結合。

print(f"Hello {joined_names}.")		# "Hello "を先頭に、"." を付けて出力