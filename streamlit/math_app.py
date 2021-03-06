import streamlit as st
import numpy as np


def home():
    st.title("math_app")
    st.write("情報数学基礎プログラミング課題")
    st.markdown(
        f"""
    > ### 目次
    * lesson01 - 四則演算
    * lesson02 - ユークリッドの互除法
    * lesson03 - 一次不定方程式
    * lesson04 - ax≡1 (mod N)
    * lesson05 - 逆行列
    * lesson06 - 連立方程式
    * lesson08 - Nを法とした行列を用いた暗号
    * lesson09 - RSA暗号

    サイドバーより各ページへ移動
    """
    )


def page01():
    st.title("lesson01 - 四則演算")

    a = st.number_input("a = ", key=int, step=1)
    b = st.number_input("b = ", key=int, step=1)

    if st.button("実行"):

        st.write("加算")
        st.write(a + b)
        st.write("減算")
        st.write(a - b)
        st.write("乗算")
        st.write(a * b)
        st.write("除算")
        st.write(a / b)
        st.write("剰余")
        st.write(a % b)
        st.write("べき乗")
        st.write(a**b)


def page02():
    st.title("lesson02 - ユークリッドの互除法")
    st.write("整数x1とx2の最大公約数を求める")

    # 途中経過を入れる配列
    a = []  # 割られる数
    b = []  # 割る数
    q = []  # 商
    r = []  # 余り
    kx = []  # xの係数
    ky = []  # yの係数

    i = 0  # リストの先頭に位置する
    j = 0  # リストの先頭に位置する

    a.append(st.number_input("x1 = ", key=int, step=1, min_value=1))
    b.append(st.number_input("x2 = ", key=int, step=1, min_value=1))

    if st.button("実行"):

        q.append(a[i] // b[i])
        r.append(a[i] % b[i])
        st.write(f"({i}) {a[i]} = {b[i]} * {q[i]} + {r[i]}")

        while r[i] != 0:
            a.append(b[i])  # 割られる数を割る数にする
            b.append(r[i])  # 割る数をあまりにする
            i += 1  # リストの位置を一つ更新
            q.append(a[i] // b[i])
            r.append(a[i] % b[i])
            st.write(f"({i}) {a[i]} = {b[i]} * {q[i]} + {r[i]}")

        st.markdown("---")
        st.write(f"最大公約数は{b[i]}")


def page03():
    st.title("lesson03 - 一次不定方程式")
    st.latex("ax + by = 1")

    # 途中経過を入れる配列
    a = []  # 割られる数
    b = []  # 割る数
    q = []  # 商
    r = []  # 余り
    kx = []  # xの係数
    ky = []  # yの係数

    i = 0  # リストの先頭に位置する
    j = 0  # リストの先頭に位置する

    a.append(st.number_input("a = ", key=int, step=1, min_value=1))
    b.append(st.number_input("b = ", key=int, step=1, min_value=1))

    if st.button("実行"):

        q.append(a[i] // b[i])
        r.append(a[i] % b[i])
        st.write(f"({i}) {a[i]} = {b[i]} * {q[i]} + {r[i]}")

        while r[i] != 0:
            a.append(b[i])  # 割られる数を割る数にする
            b.append(r[i])  # 割る数をあまりにする
            i += 1  # リストの位置を一つ更新
            q.append(a[i] // b[i])
            r.append(a[i] % b[i])
            st.write(f"({i}) {a[i]} = {b[i]} * {q[i]} + {r[i]}")

        st.write(f"最大公約数は{b[i]}")
        st.write("一次不定方程式を解く")

        i -= 1
        kx.append(1)
        ky.append(-q[i])
        st.write(f"({i}) 1 = ({kx[j]}) * {a[i]} + ({ky[j]}) * {b[i]}")

        # 0行目まで繰り返す
        while i != 0:
            i -= 1  # 一行下へ
            kx.append(ky[j])
            ky.append(kx[j] + (q[i]) * (-ky[j]))
            j += 1  # リストの位置を一つ更新
            st.write(f"({i})　= ({kx[j]}) * {a[i]} + ({ky[j]}) * {b[i]}")

        # 結果を出力
        st.markdown("---")
        st.write(f"{a[i]} x + {b[i]}y = 1の解は")
        st.write(f"特殊解 x0 = {kx[j]}, y0 = {ky[j]}")
        st.write(f"x = {kx[j]} + {b[i]} *t")
        st.write(f"x = {ky[j]} - {a[i]} *t")


def page04():
    st.title("lesson04 - ax≡1 (mod N)")
    st.latex("ax≡ (mod N)")
    st.write("この時のxを求める。")

    a = []  # 割られる数
    mod = []  # 割る数
    q = []  # 商
    r = []  # 余り
    kx = []  # xの係数
    ky = []  # yの係数
    i = 0  # リストの先頭に位置する
    j = 0  # リストの先頭に位置する

    # 値を入力
    a.append(st.number_input("a = ", key=int, step=1, min_value=1))
    mod.append(st.number_input("mod = ", key=int, step=1, min_value=1))

    # 実行ボタンを押してから計算を始める
    if st.button("実行"):

        q.append(a[i] // mod[i])
        r.append(a[i] % mod[i])
        st.write(f"({i}) {a[i]} = {mod[i]} * {q[i]} + {r[i]}")

        while r[i] != 0:
            a.append(mod[i])  # 割られる数を割る数にする
            mod.append(r[i])  # 割る数をあまりにする
            i += 1  # リストの位置を一つ更新
            q.append(a[i] // mod[i])
            r.append(a[i] % mod[i])
            st.write(f"({i}) {a[i]} = {mod[i]} * {q[i]} + {r[i]}")

        st.write(f"最大公約数は{mod[i]}")
        st.write("一次不定方程式を解く")

        i -= 1
        kx.append(1)
        ky.append(-q[i])
        st.write(f"({i}) 1 = ({kx[j]}) * {a[i]} + ({ky[j]}) * {mod[i]}")

        # 0行目まで繰り返す
        while i != 0:
            i -= 1  # 一行下へ
            kx.append(ky[j])
            ky.append(kx[j] + (q[i]) * (-ky[j]))
            j += 1  # リストの位置を一つ更新
            st.write(f"({i})　= ({kx[j]}) * {a[i]} + ({ky[j]}) * {mod[i]}")

        # 結果を出力
        st.markdown("---")
        st.write(f"{a[i]} x ≡ 1 mod({mod[i]}) の解は")
        st.write(f"x ≡ {kx[j]}, y ≡ {ky[j]} mod ({mod[i]})")


def page05():
    st.title("lesson05 - 逆行列")

    st.latex(
        r"""
    \begin{pmatrix}
    a00 & a01 \\
    a10 & a11 \\
    \end{pmatrix} (modN)
    """
    )

    st.write("この時の逆行列を求める。")

    a = []  # 割られる数
    b = []  # 割る数
    q = []  # 商
    r = []  # 余り
    kx = []  # xの係数
    ky = []  # yの係数
    i = 0  # リストの先頭に位置する
    j = 0  # リストの先頭に位置する

    # numpy配列を宣言、初期化
    arr = np.array([[0, 1], [2, 3]])

    # 値を入力
    arr[0][0] = int(st.number_input("a00 = ", key=int, step=1))
    arr[0][1] = int(st.number_input("a01 = ", key=int, step=1))
    arr[1][0] = int(st.number_input("a10 = ", key=int, step=1))
    arr[1][1] = int(st.number_input("a11 = ", key=int, step=1))
    mod = int(st.number_input("mod = ", key=int, step=1))

    # 実行ボタンを押してから計算を始める
    if st.button("実行"):

        # インバース|A|を求める
        a.append((arr[0][0] * arr[1][1]) - (arr[0][1] * arr[1][0]) % mod)
        b.append(mod)
        q.append(a[i] // b[i])  # 商をリストの先頭に追加
        r.append(a[i] % b[i])  # 余りをリストの先頭に追加

        while r[i] != 0:
            a.append(b[i])  # 割られる数を割る数にする
            b.append(r[i])  # 割る数をあまりにする
            i += 1  # リストの位置を一つ更新
            q.append(a[i] // b[i])
            r.append(a[i] % b[i])

        i -= 1
        kx.append(1)
        ky.append(-q[i])

        while i != 0:
            i -= 1  # 一行下へ
            kx.append(ky[j])
            ky.append(kx[j] + (q[i]) * (-ky[j]))
            j += 1  # リストの位置を一つ更新

        # 求めたインバース|A|をaに代入
        a = kx[j]

        # Nを法とした逆数
        arr_inv = np.array([[arr[1][1], -arr[0][1]], [-arr[1][0], arr[0][0]]])
        ans = arr_inv * a  # 逆行列

        st.write("入力された行列")
        st.write(arr)
        st.write(arr_inv)
        st.write(ans)

        # 最小正剰余の計算
        ans = ans % mod

        # 結果の出力
        st.markdown("---")
        st.write(f"逆行列(mod{mod} )")
        st.write(ans)


def page06():

    st.title("lesson06 - 連立方程式")
    st.latex(
        r"""
    \begin{pmatrix}
    a00 & a01 \\
    a10 & a11 \\
    \end{pmatrix} * 
    
    \begin{pmatrix}
    x \\
    y \\
    \end{pmatrix} ≡
    
    \begin{pmatrix}
    a \\
    b \\
    \end{pmatrix} (modN)
    """
    )

    st.write("この時の(x, y)を求める。")

    a = []  # 割られる数
    b = []  # 割る数
    q = []  # 商
    r = []  # 余り
    kx = []  # xの係数
    ky = []  # yの係数
    i = 0  # リストの先頭に位置する
    j = 0  # リストの先頭に位置する

    # numpy配列を宣言、初期化
    arr = np.array([[0, 1], [2, 3]])
    arr_ab = np.array([[1], [2]])

    # 値を入力
    arr[0][0] = int(st.number_input("a00 = ", key=int, step=1))
    arr[0][1] = int(st.number_input("a01 = ", key=int, step=1))
    arr[1][0] = int(st.number_input("a10 = ", key=int, step=1))
    arr[1][1] = int(st.number_input("a11 = ", key=int, step=1))
    arr_ab[0][0] = int(st.number_input("a = ", key=int, step=1))
    arr_ab[1][0] = int(st.number_input("b = ", key=int, step=1))
    mod = int(st.number_input("mod = ", key=int, step=1))

    if st.button("実行"):

        # インバース|A|を求める
        a.append((arr[0][0] * arr[1][1]) - (arr[0][1] * arr[1][0]) % mod)
        b.append(mod)
        q.append(a[i] // b[i])  # 商をリストの先頭に追加
        r.append(a[i] % b[i])  # 余りをリストの先頭に追加

        while r[i] != 0:
            a.append(b[i])  # 割られる数を割る数にする
            b.append(r[i])  # 割る数をあまりにする
            i += 1  # リストの位置を一つ更新
            q.append(a[i] // b[i])
            r.append(a[i] % b[i])

        i -= 1
        kx.append(1)
        ky.append(-q[i])

        while i != 0:
            i -= 1  # 一行下へ
            kx.append(ky[j])
            ky.append(kx[j] + (q[i]) * (-ky[j]))
            j += 1  # リストの位置を一つ更新

        # 求めたインバース|A|を代入
        a = kx[j]

        # Nを法とした逆数
        arr_inv = np.array([[arr[1][1], -arr[0][1]], [-arr[1][0], arr[0][0]]])
        temp = arr_inv * a  # 逆行列

        # 最小正剰余の計算
        temp = temp % mod

        # 結果の出力
        st.write("行列")
        st.write(arr)
        st.write("逆行列")
        st.write(temp)

        # 配列の積
        ans = np.dot(temp, arr_ab)

        # 最小正剰余の計算
        ans = ans % mod

        # 結果の出力
        st.markdown("---")
        st.write(f"{mod} を法とした")
        st.write(f"(x, y) (mod{mod}) は")
        st.write(ans)


def page08():

    a = []  # 割られる数
    b = []  # 割る数
    q = []  # 商
    r = []  # 余り
    kx = []  # xの係数
    ky = []  # yの係数
    i = 0  # リストの先頭に位置する
    j = 0  # リストの先頭に位置する

    st.title("lesson08 - 連立方程式")
    st.write("復号化する暗号文の入力は")
    st.latex(
        r"""
        \begin{pmatrix}
        x11 & x12 \\
        x21 & x22 \\
        \end{pmatrix} or 
        \begin{pmatrix}
        x11 & x12 & x13 \\
        x21 & x22 & x23 \\
        \end{pmatrix}
        """
    )
    st.write("とし、入力の順番は **x11 ,x12, x13, x21 ,x22 ,x23** とする。")
    st.write("arr_aは平文の一部、arr_bは暗号文の一部とする。")
    st.write("文字列に対応する数値は以下の表から得る。")
    st.image(
        "data:image/png;base64,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"
    )

    # numpy配列を宣言、初期化
    arr_p = np.array([[1, 2], [3, 4]])
    arr_c = np.array([[1, 2], [3, 4]])

    # 入力
    st.write("平文の一部を入力")
    arr_p[0][0] = int(st.number_input("Enter a11: ", key=int, step=1))
    arr_p[0][1] = int(st.number_input("Enter a12: ", key=int, step=1))
    arr_p[1][0] = int(st.number_input("Enter a21: ", key=int, step=1))
    arr_p[1][1] = int(st.number_input("Enter a22", key=int, step=1))
    st.write("暗号文の一部を入力")
    arr_c[0][0] = int(st.number_input("Enter b11: ", key=int, step=1))
    arr_c[0][1] = int(st.number_input("Enter b12: ", key=int, step=1))
    arr_c[1][0] = int(st.number_input("Enter b21: ", key=int, step=1))
    arr_c[1][1] = int(st.number_input("Enter b22: ", key=int, step=1))
    mod = int(st.number_input("Enter mod: ", key=int, step=1))

    # 復号化したい暗号文を入力
    # 暗号文が4文字か6文字か選択する
    st.write("復号化したい暗号文の文字数を入力(4 or 6)")
    ifWordCount = int(st.number_input("Enter 4 or 6: ", key=int, step=1))
    if ifWordCount == 4:
        arr_C = np.array([[1, 2], [3, 4]])
        arr_C[0][0] = int(st.number_input("Enter x11: ", key=int, step=1))
        arr_C[0][1] = int(st.number_input("Enter x12: ", key=int, step=1))
        arr_C[1][0] = int(st.number_input("Enter x21: ", key=int, step=1))
        arr_C[1][1] = int(st.number_input("Enter x22: ", key=int, step=1))
    elif ifWordCount == 6:
        arr_C = np.array([[1, 2, 3], [4, 5, 6]])
        arr_C[0][0] = int(st.number_input("Enter x11: ", key=int, step=1))
        arr_C[0][1] = int(st.number_input("Enter x12: ", key=int, step=1))
        arr_C[0][2] = int(st.number_input("Enter x13: ", key=int, step=1))
        arr_C[1][0] = int(st.number_input("Enter x21: ", key=int, step=1))
        arr_C[1][1] = int(st.number_input("Enter x22: ", key=int, step=1))
        arr_C[1][2] = int(st.number_input("Enter x23: ", key=int, step=1))

    if st.button("実行"):

        # インバース|A|を求める
        a.append((arr_p[0][0] * arr_p[1][1]) - (arr_p[0][1] * arr_p[1][0]) % mod)
        b.append(mod)
        q.append(a[i] // b[i])  # 商をリストの先頭に追加
        r.append(a[i] % b[i])  # 余りをリストの先頭に追加

        while r[i] != 0:
            a.append(b[i])  # 割られる数を割る数にする
            b.append(r[i])  # 割る数をあまりにする
            i += 1  # リストの位置を一つ更新
            q.append(a[i] // b[i])
            r.append(a[i] % b[i])

        i -= 1
        kx.append(1)
        ky.append(-q[i])

        while i != 0:
            i -= 1  # 一行下へ
            kx.append(ky[j])
            ky.append(kx[j] + (q[i]) * (-ky[j]))
            j += 1  # リストの位置を一つ更新

        # 求めたインバース|A|を代入
        a = kx[j]

        # Nを法とした逆数
        arr_inv = np.array([[arr_p[1][1], -arr_p[0][1]], [-arr_p[1][0], arr_p[0][0]]])
        ans = arr_inv * a % mod  # 逆行列

        # 行列の積はnp.dotを使用し、暗号鍵を求める
        ans = np.dot(arr_c, ans) % mod

        # 暗号鍵を出力
        st.markdown("---")
        st.write("暗号鍵は")
        st.write(ans)

        a = []  # 割られる数
        b = []  # 割る数
        q = []  # 商
        r = []  # 余り
        kx = []  # xの係数
        ky = []  # yの係数
        i = 0  # リストの先頭に位置する
        j = 0  # リストの先頭に位置する

        # インバース|A|を求める
        a.append((ans[0][0] * ans[1][1]) - (ans[0][1] * ans[1][0]) % mod)
        b.append(mod)
        q.append(a[i] // b[i])  # 商をリストの先頭に追加
        r.append(a[i] % b[i])  # 余りをリストの先頭に追加

        while r[i] != 0:
            a.append(b[i])  # 割られる数を割る数にする
            b.append(r[i])  # 割る数をあまりにする
            i += 1  # リストの位置を一つ更新
            q.append(a[i] // b[i])
            r.append(a[i] % b[i])

        i -= 1
        kx.append(1)
        ky.append(-q[i])

        while i != 0:
            i -= 1  # 一行下へ
            kx.append(ky[j])
            ky.append(kx[j] + (q[i]) * (-ky[j]))
            j += 1  # リストの位置を一つ更新

        # 求めたインバース|A|を代入
        a = kx[j]

        # Nを法とした逆数
        arr_inv = np.array([[ans[1][1], -ans[0][1]], [-ans[1][0], ans[0][0]]])
        ans = arr_inv * a % mod  # 逆行列

        # 復号鍵を出力
        st.write("復号鍵は")
        st.write(ans)

        # 行列の積はnp.dotを使用し、復号化
        ans = np.dot(ans, arr_C) % mod

        # 復号化
        st.write("---")
        st.write("復号化された数値")
        st.image(
            "data:image/png;base64,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"
        )
        st.write(ans)


def page09():

    st.title("lesson09 - RSA暗号")

    n = int(st.number_input("Enter n: ", key=int, step=1))
    e = int(st.number_input("Enter e: ", key=int, step=1))
    plaintext = str(st.text_input("Enter Plaintext: ", key=str))
    template = str(st.text_input("Enter Template: ", key=str))
    if st.button("実行"):
        n_shin = len(template)  # len関数で文字数NをN進数とする

        result = 0  # 初期化
        # 平文を１つの数字にする(N進数10進数変換)
        for i in range(len(plaintext)):
            for j in range(len(template)):
                if plaintext[i] == template[j]:
                    result += j * (len(template) ** (len(plaintext) - i - 1))

        # 平文を数字にしたものをPとする
        P = result

        # PをCとして暗号化する
        C = (P**e) % n

        # Cを10進数からN進数に変換
        C = np.base_repr(C, n_shin)

        crypttext = ""  # 暗号文の文字列の初期化
        # Cを文字列にする
        for i in range(len(C)):
            j = 0
            for j in range(len(template)):
                if int(C[i]) == int(j):
                    crypttext += template[j]

        st.write(f"{plaintext}を暗号化すると{crypttext}")


# 複数ページを管理
pagelist = [
    "home",
    "lesson01 - 四則演算",
    "lesson02 - ユークリッドの互除法",
    "lesson03 - 一次不定方程式",
    "lesson04 - ax≡1 (mod N)",
    "lesson05 - 逆行列",
    "lesson06 - 連立方程式",
    "lesson08 - Nを法とした行列を用いた暗号",
    "lesson09 - RSA暗号",
]

# サイドバー管理
sidebar = st.sidebar.selectbox(
    ("ページ選択"), pagelist
)  # サイドバーを定義し、selectboxで選択する方式にする。pagelistを参照する。
if sidebar == "lesson01 - 四則演算":
    page01()

if sidebar == "lesson02 - ユークリッドの互除法":
    page02()

if sidebar == "lesson03 - 一次不定方程式":
    page03()

if sidebar == "lesson04 - ax≡1 (mod N)":
    page04()

if sidebar == "lesson05 - 逆行列":
    page05()

if sidebar == "lesson06 - 連立方程式":
    page06()

if sidebar == "lesson08 - Nを法とした行列を用いた暗号":
    page08()

if sidebar == "lesson09 - RSA暗号":
    page09()

if sidebar == "home":
    home()
