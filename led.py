# -*- coding: utf-8 -*-
#GPIOを制御するライブラリ
import wiringpi
#タイマーのライブラリ
import time
 
# LEDを繋いだGPIOの端子番号
led_pin = 26 # 3番端子
 
# GPIO初期化
wiringpi.wiringPiSetupGpio()
# GPIOを出力モード（1）に設定
wiringpi.pinMode( led_pin, 1 )
 
# whileの無限ループ
while True:
# GPIOを3.3VにしてLEDを点灯
    wiringpi.digitalWrite( led_pin, 1 )
    # 1秒待ち
    time.sleep(1)
    # GPIOを0VにしてLEDを消灯
    wiringpi.digitalWrite( led_pin, 0 )
    # 1秒待ち
    time.sleep(1)

