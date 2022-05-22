import streamlit as st
import pandas as pd
import numpy as np

def main():

    st.title("連立方程式")
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

if __name__ == "__main__":
    main()
