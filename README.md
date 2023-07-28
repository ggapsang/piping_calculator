# Calculator for Piping and Pipefitter

It performs 4 arithmetic operations like a general calculator, but if you enter piping material specifications instead of numbers (ex: 2 10-inch elbows + 10*6 reducer), it finds the length of the material in the database and converts it into numbers to perform calculations.
(Material specifications are stored in .csv file format based on ASTM standards)

For example, in case of jointing two 10-inch pipe 5000 and bw type 10-inch elbow, to find the total length when combining two of them, the general calculator calculates as follows.

  5000 + 38.1*10*2 = 5762

Since the formula for calculating the value of a 90 degree elbow is simple, this calculation is not a problem. However, there is no case of memorizing the length of fittings such as special angles (elbow values ​​of angles other than 90 and 45 degrees), tees, and reducers. Therefore, at the site, I look at the fitting and measure it myself and then add it, or I search the catalog to check the value and then add it. However, for this program, enter the command as follows.

  5000 + elbow(10)*2 = 5762

In addition, not only elbows, but all fittings, valves, flanges, tees, etc. are possible if the user accurately writes the command.

# 배관용_계산기

일반적인 계산기와 같이 사칙연산을 수행하지만, 숫자 대신 배관 자재 스펙을 입력하면(ex 10인치 엘보 2개 + 10*6 레듀샤) 데이터베이스에서 해당 자재의 기장을 찾아 숫자로 바꿔 연산을 수행한다.
(자재 스펙은 ASTM 기준으로 .csv 파일 형태로 저장되어 있음)

예를 들어, 10인치 파이프 5000, bw 타입 10인치 엘보 두개를 조인트 할 경우중 2개를 결합할 경우 총 기장을 구하려면 일반 계산기에서는 아래와 같이 계산한다.

  5000 + 38.1*10*2 = 5762

90도 엘보값을 구하는 공식은 간단하기 때문에 이런 계산은 문제가 없다. 하지만 특수각(90, 45도 외의 각도의 엘보값)이나 티, 레듀샤 등의 피팅류의 기장값을 외우고 다니는 경우는 없다. 그렇기 때문에 현장에서는 피팅을 보고 직접 치수를 잰 뒤 더하거나, 카탈로그를 뒤져서 값을 확인 한 뒤 더한다. 그러나 이 프로그램의 경우 아래와 같이 커맨드를 입력한다.

  5000 + elbow(10)*2 = 5762

또한 엘보뿐만 아니라 모든 피팅, 밸브, 플랜지, 티 등 사용자가 정확하게 명령을 작성하면 가능하다.




