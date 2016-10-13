#yehh
class l1_provider():
    def __init__(self):
        pass
    def l1_service():
        raise NotImplementedError

class l2_provider():
    def __init__(self):
        self.l1 = None
    def set_lower_layer(self,l1_provider):
        self.l1 = l1_provider
    def l2_service():
        raise NotImplementedError

class l3_provider():
    def __init__(self):
        self.l2 = None
    def set_lower_layer(self,l2_provider):
        self.l2 = l2_provider
    def l3_service():
        raise NotImplementedError

class data_link(l1_provider):
    def __init__(self):
        pass
    def l1_service(self):
        print("service 1 doing it's job")

class transport(l2_provider):
    def __init__(self):
        self.l1 = None
    def l2_service(self):
        print("service 2 running")
        self.l1.l1_service()
        print("service 2 ending")

class session(l3_provider):
    def __init__(self):
        self.l2 = None
    def l3_service(self):
        print("service 3 running")
        self.l2.l2_service()
        print("service 3 ending")

#main
data_link_var = data_link()
transport_var = transport()
session_var = session()

transport_var.set_lower_layer(data_link_var)
session_var.set_lower_layer(transport_var)

session_var.l3_service()
