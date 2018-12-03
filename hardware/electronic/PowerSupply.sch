EESchema Schematic File Version 4
LIBS:LMRHAT-cache
EELAYER 26 0
EELAYER END
$Descr USLetter 11000 8500
encoding utf-8
Sheet 3 3
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector_Generic:Conn_01x02 J?
U 1 1 5C10590C
P 10100 3800
AR Path="/5C10590C" Ref="J?"  Part="1" 
AR Path="/5C0F7799/5C10590C" Ref="J8"  Part="1" 
F 0 "J8" V 10066 3880 50  0000 L CNN
F 1 "Battery Connector" V 9975 3880 50  0000 L CNN
F 2 "Connector_JST:JST_EH_B02B-EH-A_1x02_P2.50mm_Vertical" H 10100 3800 50  0001 C CNN
F 3 "http://www.jst-mfg.com/product/pdf/eng/eEH.pdf" H 10100 3800 50  0001 C CNN
	1    10100 3800
	1    0    0    -1  
$EndComp
Text Label 9600 3800 0    50   ~ 0
BATT+
Wire Wire Line
	9600 3900 9900 3900
$Comp
L Battery_Management:MCP73831-2-OT U?
U 1 1 5C10592A
P 8500 3600
AR Path="/5C10592A" Ref="U?"  Part="1" 
AR Path="/5C0F7799/5C10592A" Ref="U7"  Part="1" 
F 0 "U7" H 8500 4078 50  0000 C CNN
F 1 "MCP73831-2-OT" H 8500 3987 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23-5_HandSoldering" H 8550 3350 50  0001 L CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/20001984g.pdf" H 8350 3550 50  0001 C CNN
	1    8500 3600
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R?
U 1 1 5C105933
P 7550 3700
AR Path="/5C105933" Ref="R?"  Part="1" 
AR Path="/5C0F7799/5C105933" Ref="R18"  Part="1" 
F 0 "R18" V 7345 3700 50  0000 C CNN
F 1 "2k" V 7436 3700 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 7590 3690 50  0001 C CNN
F 3 "~" H 7550 3700 50  0001 C CNN
	1    7550 3700
	0    1    1    0   
$EndComp
$Comp
L Device:C_Small C?
U 1 1 5C10594A
P 8000 3500
AR Path="/5C10594A" Ref="C?"  Part="1" 
AR Path="/5C0F7799/5C10594A" Ref="C10"  Part="1" 
F 0 "C10" H 8092 3546 50  0000 L CNN
F 1 "0.1 uF" H 8092 3455 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 8000 3500 50  0001 C CNN
F 3 "~" H 8000 3500 50  0001 C CNN
	1    8000 3500
	-1   0    0    -1  
$EndComp
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C105974
P 9600 4400
AR Path="/5C105974" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C105974" Ref="#PWR0125"  Part="1" 
F 0 "#PWR0125" H 9600 4150 50  0001 C CNN
F 1 "GND" H 9605 4227 50  0000 C CNN
F 2 "" H 9600 4400 50  0000 C CNN
F 3 "" H 9600 4400 50  0000 C CNN
	1    9600 4400
	1    0    0    -1  
$EndComp
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C10597A
P 8500 3950
AR Path="/5C10597A" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C10597A" Ref="#PWR0126"  Part="1" 
F 0 "#PWR0126" H 8500 3700 50  0001 C CNN
F 1 "GND" H 8505 3777 50  0000 C CNN
F 2 "" H 8500 3950 50  0000 C CNN
F 3 "" H 8500 3950 50  0000 C CNN
	1    8500 3950
	1    0    0    -1  
$EndComp
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C105985
P 8000 3850
AR Path="/5C105985" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C105985" Ref="#PWR0127"  Part="1" 
F 0 "#PWR0127" H 8000 3600 50  0001 C CNN
F 1 "GND" H 8005 3677 50  0000 C CNN
F 2 "" H 8000 3850 50  0000 C CNN
F 3 "" H 8000 3850 50  0000 C CNN
	1    8000 3850
	1    0    0    -1  
$EndComp
$Comp
L Analog_ADC:MCP3421A0T-ECH U?
U 1 1 5C10598E
P 8400 5650
AR Path="/5C10598E" Ref="U?"  Part="1" 
AR Path="/5C0F7799/5C10598E" Ref="U6"  Part="1" 
F 0 "U6" H 8400 6228 50  0000 C CNN
F 1 "MCP3421A0T-ECH" H 8400 6137 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23-6_Handsoldering" H 8400 5650 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/22003e.pdf" H 8400 5650 50  0001 C CNN
	1    8400 5650
	-1   0    0    -1  
$EndComp
$Comp
L Device:R_US R?
U 1 1 5C105995
P 9400 5300
AR Path="/5C105995" Ref="R?"  Part="1" 
AR Path="/5C0F7799/5C105995" Ref="R20"  Part="1" 
F 0 "R20" V 9195 5300 50  0000 C CNN
F 1 "1m" V 9286 5300 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9440 5290 50  0001 C CNN
F 3 "~" H 9400 5300 50  0001 C CNN
	1    9400 5300
	-1   0    0    1   
$EndComp
Wire Wire Line
	8900 5550 9400 5550
Wire Wire Line
	9400 5550 9400 5450
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C10599F
P 8900 6050
AR Path="/5C10599F" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C10599F" Ref="#PWR0128"  Part="1" 
F 0 "#PWR0128" H 8900 5800 50  0001 C CNN
F 1 "GND" H 8905 5877 50  0000 C CNN
F 2 "" H 8900 6050 50  0000 C CNN
F 3 "" H 8900 6050 50  0000 C CNN
	1    8900 6050
	1    0    0    -1  
$EndComp
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C1059A5
P 8400 6050
AR Path="/5C1059A5" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C1059A5" Ref="#PWR0130"  Part="1" 
F 0 "#PWR0130" H 8400 5800 50  0001 C CNN
F 1 "GND" H 8405 5877 50  0000 C CNN
F 2 "" H 8400 6050 50  0000 C CNN
F 3 "" H 8400 6050 50  0000 C CNN
	1    8400 6050
	1    0    0    -1  
$EndComp
Wire Wire Line
	8900 5750 8900 6050
$Comp
L Device:C_Small C?
U 1 1 5C1059B2
P 7400 5400
AR Path="/5C1059B2" Ref="C?"  Part="1" 
AR Path="/5C0F7799/5C1059B2" Ref="C9"  Part="1" 
F 0 "C9" H 7492 5446 50  0000 L CNN
F 1 "0.1 uF" H 7492 5355 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 7400 5400 50  0001 C CNN
F 3 "~" H 7400 5400 50  0001 C CNN
	1    7400 5400
	1    0    0    1   
$EndComp
$Comp
L power:+3.3V #Vpi?
U 1 1 5C1059BF
P 7400 5100
AR Path="/5C1059BF" Ref="#Vpi?"  Part="1" 
AR Path="/5C0F7799/5C1059BF" Ref="#Vpi0105"  Part="1" 
F 0 "#Vpi0105" H 7400 4950 50  0001 C CNN
F 1 "+3.3V" H 7400 5240 50  0000 C CNN
F 2 "" H 7400 5100 50  0000 C CNN
F 3 "" H 7400 5100 50  0000 C CNN
	1    7400 5100
	1    0    0    -1  
$EndComp
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C1059C9
P 7400 5550
AR Path="/5C1059C9" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C1059C9" Ref="#PWR0132"  Part="1" 
F 0 "#PWR0132" H 7400 5300 50  0001 C CNN
F 1 "GND" H 7405 5377 50  0000 C CNN
F 2 "" H 7400 5550 50  0000 C CNN
F 3 "" H 7400 5550 50  0000 C CNN
	1    7400 5550
	1    0    0    -1  
$EndComp
Wire Wire Line
	7400 5500 7400 5550
$Comp
L LMRHAT:+Vopt #PWR?
U 1 1 5C1059E8
P 1800 5100
AR Path="/5C1059E8" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C1059E8" Ref="#PWR0134"  Part="1" 
F 0 "#PWR0134" H 1800 4950 50  0001 C CNN
F 1 "+Vopt" H 1815 5273 50  0000 C CNN
F 2 "" H 1800 5100 50  0000 C CNN
F 3 "" H 1800 5100 50  0000 C CNN
	1    1800 5100
	1    0    0    -1  
$EndComp
Wire Wire Line
	1800 5100 1800 5200
Text GLabel 7900 5550 0    50   Input ~ 0
SCL
Text GLabel 7900 5650 0    50   Input ~ 0
SDA
Wire Wire Line
	8500 3900 8500 3950
Wire Wire Line
	8000 3300 8000 3400
Wire Wire Line
	8000 3300 8500 3300
Text Notes 7550 3150 0    50   ~ 0
Battery Charger
Text Notes 7700 5000 0    50   ~ 0
Battery Monitor
Connection ~ 8000 3300
Text Label 9600 3900 0    50   ~ 0
BATT-
Wire Wire Line
	7400 5300 7400 5250
Wire Wire Line
	7400 5250 8400 5250
Wire Wire Line
	7400 5250 7400 5100
Connection ~ 7400 5250
Text GLabel 9200 3800 3    50   Input ~ 0
BATT_CHARGE
$Comp
L Device:R_US R?
U 1 1 5C1EFF45
P 9200 3150
AR Path="/5C1EFF45" Ref="R?"  Part="1" 
AR Path="/5C0F7799/5C1EFF45" Ref="R22"  Part="1" 
F 0 "R22" V 8995 3150 50  0000 C CNN
F 1 "10k" V 9086 3150 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9240 3140 50  0001 C CNN
F 3 "~" H 9200 3150 50  0001 C CNN
	1    9200 3150
	1    0    0    1   
$EndComp
Wire Wire Line
	9200 3700 9200 3800
$Comp
L power:+BATT #PWR0146
U 1 1 5C2021F0
P 9400 3200
F 0 "#PWR0146" H 9400 3050 50  0001 C CNN
F 1 "+BATT" H 9415 3373 50  0000 C CNN
F 2 "" H 9400 3200 50  0001 C CNN
F 3 "" H 9400 3200 50  0001 C CNN
	1    9400 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	9200 2850 9200 3000
Wire Wire Line
	9400 3200 9400 3500
Connection ~ 9400 3500
Connection ~ 1800 5200
Wire Wire Line
	2750 5200 2900 5200
Wire Wire Line
	9400 3500 9400 3800
Wire Wire Line
	9400 3800 9900 3800
Connection ~ 9400 3800
Wire Wire Line
	9400 5150 9400 3800
$Comp
L LMRHAT:MAX40200 U?
U 1 1 5C1058DD
P 3700 5250
AR Path="/5C1058DD" Ref="U?"  Part="1" 
AR Path="/5C0F7799/5C1058DD" Ref="U4"  Part="1" 
F 0 "U4" H 3700 5615 50  0000 C CNN
F 1 "MAX40200" H 3700 5524 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23-5_HandSoldering" H 3700 5400 50  0001 C CNN
F 3 "" H 3700 5400 50  0001 C CNN
	1    3700 5250
	-1   0    0    -1  
$EndComp
Text Notes 2250 4850 0    50   ~ 0
Main Power\nEnable
$Comp
L Amplifier_Operational:LMV321 U2
U 1 1 5C055640
P 2300 6700
F 0 "U2" H 2350 6850 50  0000 L CNN
F 1 "LMV321" H 2350 6550 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23-5_HandSoldering" H 2300 6700 50  0001 L CNN
F 3 "http://www.ti.com/lit/ds/symlink/lmv324.pdf" H 2300 6700 50  0001 C CNN
F 4 "497-13051-1-ND" H 2300 6700 50  0001 C CNN "Digikey"
	1    2300 6700
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C?
U 1 1 5C055829
P 2400 6300
AR Path="/5C055829" Ref="C?"  Part="1" 
AR Path="/5C0F7799/5C055829" Ref="C11"  Part="1" 
F 0 "C11" H 2492 6346 50  0000 L CNN
F 1 "0.1 uF" H 2492 6255 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 2400 6300 50  0001 C CNN
F 3 "~" H 2400 6300 50  0001 C CNN
	1    2400 6300
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2200 6400 2200 6300
Wire Wire Line
	2300 6300 2200 6300
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C0622C2
P 2600 6400
AR Path="/5C0622C2" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C0622C2" Ref="#PWR0122"  Part="1" 
F 0 "#PWR0122" H 2600 6150 50  0001 C CNN
F 1 "GND" H 2605 6227 50  0000 C CNN
F 2 "" H 2600 6400 50  0000 C CNN
F 3 "" H 2600 6400 50  0000 C CNN
	1    2600 6400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2600 6400 2600 6300
Wire Wire Line
	2600 6300 2500 6300
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C0693A3
P 2200 7100
AR Path="/5C0693A3" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C0693A3" Ref="#PWR0123"  Part="1" 
F 0 "#PWR0123" H 2200 6850 50  0001 C CNN
F 1 "GND" H 2205 6927 50  0000 C CNN
F 2 "" H 2200 7100 50  0000 C CNN
F 3 "" H 2200 7100 50  0000 C CNN
	1    2200 7100
	1    0    0    -1  
$EndComp
Wire Wire Line
	2200 7100 2200 7000
Wire Wire Line
	1800 5200 1800 6600
$Comp
L LMRHAT:+Vhandoff #PWR0124
U 1 1 5C0889E9
P 2200 5950
F 0 "#PWR0124" H 2200 5800 50  0001 C CNN
F 1 "+Vhandoff" H 2215 6123 50  0000 C CNN
F 2 "" H 2200 5950 50  0000 C CNN
F 3 "" H 2200 5950 50  0000 C CNN
	1    2200 5950
	1    0    0    -1  
$EndComp
Wire Wire Line
	2200 5950 2200 6300
Connection ~ 2200 6300
$Comp
L power:+BATT #PWR0131
U 1 1 5C0DB3A3
P 1900 6300
F 0 "#PWR0131" H 1900 6150 50  0001 C CNN
F 1 "+BATT" H 1915 6473 50  0000 C CNN
F 2 "" H 1900 6300 50  0001 C CNN
F 3 "" H 1900 6300 50  0001 C CNN
	1    1900 6300
	1    0    0    -1  
$EndComp
$Comp
L power:+BATT #PWR0133
U 1 1 5C0DB42D
P 4250 5050
F 0 "#PWR0133" H 4250 4900 50  0001 C CNN
F 1 "+BATT" H 4265 5223 50  0000 C CNN
F 2 "" H 4250 5050 50  0001 C CNN
F 3 "" H 4250 5050 50  0001 C CNN
	1    4250 5050
	1    0    0    -1  
$EndComp
Wire Wire Line
	4250 5050 4250 5200
Wire Wire Line
	4250 5200 4000 5200
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C0DDED0
P 4100 5500
AR Path="/5C0DDED0" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C0DDED0" Ref="#PWR0135"  Part="1" 
F 0 "#PWR0135" H 4100 5250 50  0001 C CNN
F 1 "GND" H 4105 5327 50  0000 C CNN
F 2 "" H 4100 5500 50  0000 C CNN
F 3 "" H 4100 5500 50  0000 C CNN
	1    4100 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	4100 5500 4100 5300
Wire Wire Line
	4100 5300 4000 5300
Text GLabel 3200 6700 2    39   Input ~ 0
CHARGE_EN
Text GLabel 1400 2300 0    50   Input ~ 0
PWR_STATUS
Text GLabel 1400 2400 0    50   Input ~ 0
SW_PWR
Wire Wire Line
	1800 2400 2100 2400
$Comp
L Device:C_Small C?
U 1 1 5C0FF1E5
P 2100 2600
AR Path="/5C0FF1E5" Ref="C?"  Part="1" 
AR Path="/5C0F7799/5C0FF1E5" Ref="C8"  Part="1" 
F 0 "C8" H 2192 2646 50  0000 L CNN
F 1 "0.1 uF" H 2192 2555 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 2100 2600 50  0001 C CNN
F 3 "~" H 2100 2600 50  0001 C CNN
	1    2100 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	2100 2500 2100 2400
Connection ~ 2100 2400
$Comp
L Device:R_US R?
U 1 1 5C102128
P 1800 2550
AR Path="/5C102128" Ref="R?"  Part="1" 
AR Path="/5C0F7799/5C102128" Ref="R17"  Part="1" 
F 0 "R17" V 1595 2550 50  0000 C CNN
F 1 "100k" V 1686 2550 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 1840 2540 50  0001 C CNN
F 3 "~" H 1800 2550 50  0001 C CNN
	1    1800 2550
	-1   0    0    1   
$EndComp
Wire Wire Line
	1400 2300 1800 2300
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C1140D4
P 2100 2800
AR Path="/5C1140D4" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C1140D4" Ref="#PWR0136"  Part="1" 
F 0 "#PWR0136" H 2100 2550 50  0001 C CNN
F 1 "GND" H 2105 2627 50  0000 C CNN
F 2 "" H 2100 2800 50  0000 C CNN
F 3 "" H 2100 2800 50  0000 C CNN
	1    2100 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	2100 2700 2100 2800
$Comp
L Device:R_US R?
U 1 1 5C12CD52
P 9400 5800
AR Path="/5C12CD52" Ref="R?"  Part="1" 
AR Path="/5C0F7799/5C12CD52" Ref="R19"  Part="1" 
F 0 "R19" V 9195 5800 50  0000 C CNN
F 1 "100k" V 9286 5800 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9440 5790 50  0001 C CNN
F 3 "~" H 9400 5800 50  0001 C CNN
	1    9400 5800
	-1   0    0    1   
$EndComp
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C12CE12
P 9400 6050
AR Path="/5C12CE12" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C12CE12" Ref="#PWR0137"  Part="1" 
F 0 "#PWR0137" H 9400 5800 50  0001 C CNN
F 1 "GND" H 9405 5877 50  0000 C CNN
F 2 "" H 9400 6050 50  0000 C CNN
F 3 "" H 9400 6050 50  0000 C CNN
	1    9400 6050
	1    0    0    -1  
$EndComp
Wire Wire Line
	9400 6050 9400 5950
Wire Wire Line
	9400 5650 9400 5550
Connection ~ 9400 5550
Wire Wire Line
	8900 3500 9400 3500
Wire Wire Line
	8900 3700 9200 3700
Wire Wire Line
	9200 3700 9200 3300
Connection ~ 9200 3700
Wire Wire Line
	8000 3600 8000 3850
Wire Wire Line
	8100 3700 7700 3700
Wire Wire Line
	6700 3300 8000 3300
Wire Wire Line
	6700 3700 7400 3700
Wire Wire Line
	2600 6700 3200 6700
Text GLabel 3700 2500 0    39   Input ~ 0
CHARGE_EN
$Comp
L Device:R_US R?
U 1 1 5C18B74D
P 1800 2150
AR Path="/5C18B74D" Ref="R?"  Part="1" 
AR Path="/5C0F7799/5C18B74D" Ref="R16"  Part="1" 
F 0 "R16" V 1595 2150 50  0000 C CNN
F 1 "100k" V 1686 2150 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 1840 2140 50  0001 C CNN
F 3 "~" H 1800 2150 50  0001 C CNN
	1    1800 2150
	-1   0    0    1   
$EndComp
Connection ~ 1800 2300
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C18B7A9
P 1600 2000
AR Path="/5C18B7A9" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C18B7A9" Ref="#PWR0138"  Part="1" 
F 0 "#PWR0138" H 1600 1750 50  0001 C CNN
F 1 "GND" H 1605 1827 50  0000 C CNN
F 2 "" H 1600 2000 50  0000 C CNN
F 3 "" H 1600 2000 50  0000 C CNN
	1    1600 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	1600 2000 1600 1900
Wire Wire Line
	1600 1900 1800 1900
Wire Wire Line
	1800 1900 1800 2000
Wire Wire Line
	1800 2700 1800 2800
$Comp
L 74xGxx:74LVC2G02 U5
U 1 1 5C1938AB
P 3500 2250
F 0 "U5" H 3475 2517 50  0000 C CNN
F 1 "74LVC2G02" H 3475 2426 50  0000 C CNN
F 2 "Package_SO:TSSOP-8_3x3mm_P0.65mm" H 3500 2250 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 3500 2250 50  0001 C CNN
	1    3500 2250
	1    0    0    -1  
$EndComp
$Comp
L 74xGxx:74LVC2G02 U5
U 2 1 5C193952
P 4200 2350
F 0 "U5" H 4175 2617 50  0000 C CNN
F 1 "74LVC2G02" H 4175 2526 50  0000 C CNN
F 2 "Package_SO:TSSOP-8_3x3mm_P0.65mm" H 4200 2350 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 4200 2350 50  0001 C CNN
F 4 "1727-5986-1-ND" H 4200 2350 50  0001 C CNN "Digikey"
	2    4200 2350
	1    0    0    -1  
$EndComp
$Comp
L 74xGxx:74LVC1G14 U3
U 1 1 5C195702
P 2800 2500
F 0 "U3" H 2775 2767 50  0000 C CNN
F 1 "74LVC1G14" H 2775 2676 50  0000 C CNN
F 2 "LMRHAT:SOT-353_SC-70-5_Handsoldering" H 2800 2500 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 2800 2500 50  0001 C CNN
F 4 "74LVC1G14SE-7CT-ND" H 2800 2500 50  0001 C CNN "Digikey"
	1    2800 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	2100 2400 2400 2400
Wire Wire Line
	2500 2500 2400 2500
Wire Wire Line
	2400 2500 2400 2400
Wire Wire Line
	3050 2500 3100 2500
Wire Wire Line
	3100 2500 3100 2300
Wire Wire Line
	3100 2300 3200 2300
Wire Wire Line
	2400 2300 2400 2100
Wire Wire Line
	2400 2100 3100 2100
Wire Wire Line
	3100 2100 3100 2200
Wire Wire Line
	3100 2200 3200 2200
Wire Wire Line
	1800 2300 2400 2300
Wire Wire Line
	1900 6800 2000 6800
Wire Wire Line
	1900 6300 1900 6800
Wire Wire Line
	1800 6600 2000 6600
Wire Wire Line
	3750 2250 3800 2250
Wire Wire Line
	3800 2250 3800 2300
Wire Wire Line
	3800 2300 3900 2300
Wire Wire Line
	3800 2500 3800 2400
Wire Wire Line
	3800 2400 3900 2400
Wire Wire Line
	3700 2500 3800 2500
Wire Wire Line
	4500 2350 4450 2350
Text GLabel 6700 3700 0    39   Input ~ 0
CHARGE_EN
$Comp
L LMRHAT:+Vopt #PWR?
U 1 1 5C1B8268
P 6700 3100
AR Path="/5C1B8268" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C1B8268" Ref="#PWR0140"  Part="1" 
F 0 "#PWR0140" H 6700 2950 50  0001 C CNN
F 1 "+Vopt" H 6715 3273 50  0000 C CNN
F 2 "" H 6700 3100 50  0000 C CNN
F 3 "" H 6700 3100 50  0000 C CNN
	1    6700 3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6700 3300 6700 3100
Text Label 4500 5800 0    39   ~ 0
PWR_EN
$Comp
L LMRHAT:TSM850N06CX Q3
U 1 1 5C1CC748
P 2550 5300
F 0 "Q3" V 2893 5300 50  0000 C CNN
F 1 "TSM850N06CX" V 2802 5300 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23_Handsoldering" H 2750 5200 50  0001 L CIN
F 3 "https://www.taiwansemi.com/products/datasheet/TSM850N06CX_B1607.pdf" H 2750 5375 50  0001 L CNN
	1    2550 5300
	0    1    -1   0   
$EndComp
Wire Wire Line
	2550 5800 2550 5500
Wire Wire Line
	2350 5200 1800 5200
Connection ~ 2900 5200
Wire Wire Line
	4000 5400 4250 5400
Wire Wire Line
	4250 5400 4250 5200
Connection ~ 4250 5200
Wire Wire Line
	2550 5800 4500 5800
Wire Wire Line
	2900 5200 3400 5200
$Comp
L Regulator_Linear:MIC5504-3.3YM5 U10
U 1 1 5C1E5D4E
P 2500 3900
F 0 "U10" H 2500 4267 50  0000 C CNN
F 1 "MIC5504-3.3YM5" H 2500 4176 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23-5_HandSoldering" H 2500 3500 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/MIC550X.pdf" H 2250 4150 50  0001 C CNN
	1    2500 3900
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2900 3800 2900 4000
Connection ~ 2900 4000
Wire Wire Line
	2900 4000 2900 5200
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C1EA973
P 2500 4300
AR Path="/5C1EA973" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C1EA973" Ref="#PWR0141"  Part="1" 
F 0 "#PWR0141" H 2500 4050 50  0001 C CNN
F 1 "GND" H 2505 4127 50  0000 C CNN
F 2 "" H 2500 4300 50  0000 C CNN
F 3 "" H 2500 4300 50  0000 C CNN
	1    2500 4300
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 4300 2500 4200
$Comp
L LMRHAT:+Vhandoff #PWR0149
U 1 1 5C1ED985
P 1900 3600
F 0 "#PWR0149" H 1900 3450 50  0001 C CNN
F 1 "+Vhandoff" H 1915 3773 50  0000 C CNN
F 2 "" H 1900 3600 50  0000 C CNN
F 3 "" H 1900 3600 50  0000 C CNN
	1    1900 3600
	1    0    0    -1  
$EndComp
Wire Wire Line
	1900 3600 1900 3800
Wire Wire Line
	1900 3800 2100 3800
Wire Wire Line
	4500 2350 4500 5800
$Comp
L Device:C_Small C?
U 1 1 5C1F4A82
P 5000 1900
AR Path="/5C1F4A82" Ref="C?"  Part="1" 
AR Path="/5C0F7799/5C1F4A82" Ref="C12"  Part="1" 
F 0 "C12" H 5092 1946 50  0000 L CNN
F 1 "0.1 uF" H 5092 1855 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 5000 1900 50  0001 C CNN
F 3 "~" H 5000 1900 50  0001 C CNN
	1    5000 1900
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C?
U 1 1 5C1F75F2
P 5500 1900
AR Path="/5C1F75F2" Ref="C?"  Part="1" 
AR Path="/5C0F7799/5C1F75F2" Ref="C13"  Part="1" 
F 0 "C13" H 5592 1946 50  0000 L CNN
F 1 "0.1 uF" H 5592 1855 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 5500 1900 50  0001 C CNN
F 3 "~" H 5500 1900 50  0001 C CNN
	1    5500 1900
	1    0    0    -1  
$EndComp
$Comp
L LMRHAT:+Vhandoff #PWR0150
U 1 1 5C1F7656
P 5000 1700
F 0 "#PWR0150" H 5000 1550 50  0001 C CNN
F 1 "+Vhandoff" H 5015 1873 50  0000 C CNN
F 2 "" H 5000 1700 50  0000 C CNN
F 3 "" H 5000 1700 50  0000 C CNN
	1    5000 1700
	1    0    0    -1  
$EndComp
$Comp
L LMRHAT:+Vhandoff #PWR0151
U 1 1 5C1F776D
P 5500 1700
F 0 "#PWR0151" H 5500 1550 50  0001 C CNN
F 1 "+Vhandoff" H 5515 1873 50  0000 C CNN
F 2 "" H 5500 1700 50  0000 C CNN
F 3 "" H 5500 1700 50  0000 C CNN
	1    5500 1700
	1    0    0    -1  
$EndComp
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C1F77D8
P 5000 2100
AR Path="/5C1F77D8" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C1F77D8" Ref="#PWR0152"  Part="1" 
F 0 "#PWR0152" H 5000 1850 50  0001 C CNN
F 1 "GND" H 5005 1927 50  0000 C CNN
F 2 "" H 5000 2100 50  0000 C CNN
F 3 "" H 5000 2100 50  0000 C CNN
	1    5000 2100
	1    0    0    -1  
$EndComp
$Comp
L LMRHAT:GND #PWR?
U 1 1 5C1F7961
P 5500 2100
AR Path="/5C1F7961" Ref="#PWR?"  Part="1" 
AR Path="/5C0F7799/5C1F7961" Ref="#PWR0153"  Part="1" 
F 0 "#PWR0153" H 5500 1850 50  0001 C CNN
F 1 "GND" H 5505 1927 50  0000 C CNN
F 2 "" H 5500 2100 50  0000 C CNN
F 3 "" H 5500 2100 50  0000 C CNN
	1    5500 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	5000 1700 5000 1800
Wire Wire Line
	5000 2000 5000 2100
Wire Wire Line
	5500 2000 5500 2100
Wire Wire Line
	5500 1700 5500 1800
Text Notes 2400 1800 0    50   ~ 0
Power Switch Debouncer
Text Notes 3150 7100 0    39   ~ 0
Note:\nCHARGE_EN is HIGH when Vopt exceeds BATT+. This signals\nthat the Pi is being powered by an external source, so the\nbattery should be disconnected and the charger enabled.
$Comp
L LMRHAT:+Vhandoff #PWR0139
U 1 1 5C20F628
P 1500 2800
F 0 "#PWR0139" H 1500 2650 50  0001 C CNN
F 1 "+Vhandoff" H 1515 2973 50  0000 C CNN
F 2 "" H 1500 2800 50  0000 C CNN
F 3 "" H 1500 2800 50  0000 C CNN
	1    1500 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	1500 2800 1800 2800
Wire Wire Line
	1400 2400 1800 2400
Connection ~ 1800 2400
$Comp
L LMRHAT:+Vhandoff #PWR0147
U 1 1 5C23087A
P 4200 2000
F 0 "#PWR0147" H 4200 1850 50  0001 C CNN
F 1 "+Vhandoff" H 4215 2173 50  0000 C CNN
F 2 "" H 4200 2000 50  0000 C CNN
F 3 "" H 4200 2000 50  0000 C CNN
	1    4200 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	4200 2250 4200 2000
$Comp
L LMRHAT:+Vhandoff #PWR0148
U 1 1 5C23A73B
P 3500 1850
F 0 "#PWR0148" H 3500 1700 50  0001 C CNN
F 1 "+Vhandoff" H 3515 2023 50  0000 C CNN
F 2 "" H 3500 1850 50  0000 C CNN
F 3 "" H 3500 1850 50  0000 C CNN
	1    3500 1850
	1    0    0    -1  
$EndComp
Wire Wire Line
	3500 1850 3500 2150
Wire Wire Line
	9600 3900 9600 4400
$Comp
L LMRHAT:+3.3V #PWR0145
U 1 1 5C044873
P 9200 2850
F 0 "#PWR0145" H 9200 2700 50  0001 C CNN
F 1 "+3.3V" H 9215 3023 50  0000 C CNN
F 2 "" H 9200 2850 50  0000 C CNN
F 3 "" H 9200 2850 50  0000 C CNN
	1    9200 2850
	1    0    0    -1  
$EndComp
$EndSCHEMATC