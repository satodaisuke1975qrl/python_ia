def cleaning(date, *args):
    staffs = ''
    for person in args:
        staffs = staffs + '「' + person + '」'

    print(date + 'の清掃担当者は' + staffs + 'です')

cleaning('12月3日', '山本', '三浦')
cleaning('12月4日', '杉山', '田中', '井口')