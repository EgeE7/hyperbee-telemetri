import json

with open("telemetri.json", "r", encoding="utf-8") as f:
    veri = json.load(f)

print("=== HyperBee Telemetri ===")
print(f"Pod      : {veri['pod_id']}")
print(f"Paket no : {veri['seq']}")
print(f"Voltaj   : {veri['voltage_v']} V")
print(f"Akım     : {veri['current_a']} A")
print(f"Sıcaklık : {veri['temperature_c']} °C")
print(f"Güç      : {veri['voltage_v'] * veri['current_a']:.1f} W")