import streamlit as st
import qrcode
from PIL import Image
import numpy as np

st.title('QRコード自動生成アプリ')

url = st.text_input('QRコードを生成したいURL：')

if st.button('QRコードを生成'):
    _img = qrcode.make(url)         #生成
    _img.save('qrcode.png')         #保存
    img = Image.open('qrcode.png')  #読み込み
    st.image(img)                   #表示