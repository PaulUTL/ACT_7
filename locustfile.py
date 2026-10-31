from locust import HttpUser, task, between

class ClienteTienda(HttpUser):
    wait_time = between(1, 5)

    @task
    def comprar_producto(self):
        self.client.post("/compra", json={"precio": 100, "descuento": 10})