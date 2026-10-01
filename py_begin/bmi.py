#1 global variables and imports

#2 getting user inputs as height and weight

def get_user_inputs() :
    weight = float(input('enter your weight (kg): '))
    height = float(input('enter your height (m): '))
    return weight,height


#3 calculate bmi 

def calculate_bmi(weight, height):
    return weight // (height**2)


#4 result 


def get_bmi_result(bmi):
    if bmi < 18.5 :
        print('too skinny')
    elif 18.5 <= bmi <= 25 :
        print('normal')
    elif 25 <= bmi <= 30 :
        print('over weight')
    elif 30 <= bmi <= 35 :
        print('obese')
    else :
        print('super obese')


#5 create main fuction


def main():
    weight,height = get_user_inputs()
    bmi = calculate_bmi(weight,height)
    get_bmi_result(bmi)

main()