import websocket
import time


headers = {
    'Authorization': f'Bearer eyJrIjoiM0NuT2l6RTVSNWJKT2RGcnNVU29lV0ozVEo5cUdGQVUiLCJuIjoidGVzdCIsImlkIjoxfQ=='
}

grafana_ws = "ws://localhost:3000/api/live/ws?format=json"

# grafana_ws = "ws://localhost:3000/api/live/push/test"



ws = websocket.WebSocket(skip_utf8_validation=True, enable_multithread=False)

ws.connect(grafana_ws, header=headers)

# for idx in range(1000):
#     print(idx)
#     influx_time = int(time.time() * 1_000_000_000)
#     ws.send(f"test ype={idx} {influx_time}")
#     time.sleep(0.01)

# # ws.connect(grafana_ws, header=headers)
# # print(ws.sock_opt.timeout)
print(ws.status)
ws.close()