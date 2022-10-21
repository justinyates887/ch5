#5b
import math as m

def check_num(str): 
    while True:
        num = input(str)
        try:
            val = int(num)
            print("✅ Verification passed, system recieved: ", val)
            return val
        except ValueError:
            print("❌Invlaid entry. Please enter a whole number")

def main():
    refugees = check_num('How many refugees need to be evacuated? ')
    carry = 350
    count = 1
    exported = 0

    print(m.ceil(refugees / carry), 'trips will be needed to evacuate', refugees, 'refugees\n')

    print('REFUGEE REPORT\nTRIP     TOTAL EVACUATED\n------------------------------')
    while refugees > 0:
        if refugees < carry:
            carry = refugees
        refugees -= carry
        exported += carry
        print(count, '      ', exported)
        count += 1
    return

main()