from employee4_mod import Company, President

def main():
    company = Company()
    company.add_employee(President('井上'))
    company.add_staff('鈴木', 1.2)
    company.add_staff('佐藤', 1.1)
    print(f'合計は、{company.total_salary():,}円です。')

if __name__ == '__main__':
    main()