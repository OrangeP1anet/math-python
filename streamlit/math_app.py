import streamlit as st
import pandas as pd
import numpy as np

def page01():
    st.title("lesson01 - 四則演算")

    a = st.number_input('a = ', key=int, step=1)
    b = st.number_input('b = ', key=int, step=1)

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
        st.write(a ** b)

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

    a.append(st.number_input('x1 = ', key=int, step=1, min_value=1))
    b.append(st.number_input('x2 = ', key=int, step=1, min_value=1))

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

    a.append(st.number_input('a = ', key=int, step=1, min_value=1))
    b.append(st.number_input('b = ', key=int, step=1, min_value=1))

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
    a.append(st.number_input('a = ', key=int, step=1, min_value=1))
    mod.append(st.number_input('mod = ', key=int, step=1, min_value=1))

    #実行ボタンを押してから計算を始める
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
        st.markdown('---')
        st.write(f"{a[i]} x ≡ 1 mod({mod[i]}) の解は")
        st.write(f"x ≡ {kx[j]}, y ≡ {ky[j]} mod ({mod[i]})")

def page05():
    st.title("lesson05 - 逆行列")

    st.latex(r"""
    \begin{pmatrix}
    a00 & a01 \\
    a10 & a11 \\
    \end{pmatrix} (modN)
    """)

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
    arr[0][0] = int(st.number_input('a00 = ', key=int, step=1))
    arr[0][1] = int(st.number_input('a01 = ', key=int, step=1))
    arr[1][0] = int(st.number_input('a10 = ', key=int, step=1))
    arr[1][1] = int(st.number_input('a11 = ', key=int, step=1))
    mod = int(st.number_input('mod = ', key=int, step=1))

    #実行ボタンを押してから計算を始める
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

        #結果の出力
        st.markdown('---')
        st.write(f"逆行列(mod{mod} )")
        st.write(ans)

def page06():

    st.title("lesson06 - 連立方程式")
    st.latex(r"""
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
    """)

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
    arr[0][0] = int(st.number_input('a00 = ', key=int, step=1))
    arr[0][1] = int(st.number_input('a01 = ', key=int, step=1))
    arr[1][0] = int(st.number_input('a10 = ', key=int, step=1))
    arr[1][1] = int(st.number_input('a11 = ', key=int, step=1))
    arr_ab[0][0] = int(st.number_input('a = ', key=int, step=1))
    arr_ab[1][0] = int(st.number_input('b = ', key=int, step=1))
    mod = int(st.number_input('mod = ', key=int, step=1))

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
        st.markdown('---')
        st.write(f"{mod} を法とした")
        st.write(f"(x, y) (mod{mod}) は")
        st.write(ans)

def home():
    st.title("math_app")
    st.write("情報数学基礎プログラミング課題")
    st.markdown(f"""
    > ### 目次
    * lesson01 - 四則演算
    * lesson02 - ユークリッドの互除法
    * lesson03 - 一次不定方程式
    * lesson04 - ax≡1 (mod N)
    * lesson05 - 逆行列
    * lesson06 - 連立方程式
    
    サイドバーより各ページへ移動
    """)

#複数ページを管理
pagelist = ["home", "lesson01 - 四則演算", "lesson02 - ユークリッドの互除法", "lesson03 - 一次不定方程式", "lesson04 - ax≡1 (mod N)", "lesson05 - 逆行列", "lesson06 - 連立方程式"]

#サイドバー管理
sidebar = st.sidebar.selectbox(("ページ選択"), pagelist) #サイドバーを定義し、selectboxで選択する方式にする。pagelistを参照する。
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

if sidebar == "home":
    home()

#おまじない?
#if __name__ == "__main__":
    #page01()