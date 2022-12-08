class Account:
    
    def __init__(self,rate,start_money,withdraw_money,top_up):
        self.__rate=rate
        self.__start_money=start_money
        self.__withdraw_money=withdraw_money
        self.__top_up=top_up

    def set_rate(self,rate):
        self.__rate=rate

    def set_start_money(self,start_money):
        self.__start_money=start_money

    def set_withdraw_money(self,withdraw_money):
        self.__withdraw_money=withdraw_money

    def set_top_up(self,top_up):
        self.__top_up=top_up

    def get_rate(self):
        return self.__rate

    def get_start_money(self):
        return self.__start_money
    
    def get_withdraw_money(self):
        return self.__withdraw_money

    def get_top_up(self):
        return self.__top_up

    def get_balance(self):
        return __start_money+__top_up-__withdraw_money

    def income(self):
        return (__start_money+__top_up-__withdraw_money)+\
               ((__start_money+__top_up-__withdraw_money)*__rate))

    

