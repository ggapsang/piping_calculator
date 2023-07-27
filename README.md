# piping_calculator
배관 전용 계산기

기본적인 일반 계산기 포멧에 다음의 기능들을 추가

사이즈, 엘보값, 티값, 밸브값 등을 자동계산하여 사칙연산을 수행함 (ui 버튼으로 엘보, 티, 밸브 등의 타입을 쉽게 누를 수 있도록 지원함)

파이프, 엘보 등 각종 피팅으로 스풀을 짰을 때 커팅 플랜을 계산해줌

모바일 앱(안드로이드)으로 구현하는 것이 최종 목표

배관과 관련된 각종 추가 기능들이 들어갈 수 있게 확장성을 고려하여 설계

class Pipe, Elbow, Tee, Reducer, Cap, Flange, Valve, Coupling

Attribute size, sch, sub_size, subsize, joint_type, degree, flange_rating, flange_tyep, long_or_short, valve_type, valve_rating

Method get_outdia(), get_india(), get_thick(), get_span()
