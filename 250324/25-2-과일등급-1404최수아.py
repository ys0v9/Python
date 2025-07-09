apple_g=int(input('과일 무게(g): '))
if apple_g>=375 or apple_g<210:
    print('"판정 불가"')
elif 300<=apple_g<375:
    print('"특"')
elif 250<=apple_g<300:
    print('"상"')
else:
    print('"보통"')