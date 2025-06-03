# esphome_components
My collection of components for esphome

To use these components, use the [external components](https://esphome.io/components/external_components.html).

Example:
```yaml
external_components:
  - source:
      type: git
      url: https://github.com/ssieb/esphome_components
    components: [ component1, component2 ]
```

## Developing, Testing & Debugging
Create/activate environment by running from project root:
```bash
source scripts/setup_build_env.sh
```

To Build ESP32 firmware on your local machine for running Wokwi:
```bash
esphome compile uart_demo-ESP8266.yaml
```

## NOTE: Some components have been merged to esphome :tada:
- keypad, matrix_keypad -> [matrix_keypad](https://esphome.io/components/matrix_keypad)
- vbus -> [Resol VBus](https://esphome.io/components/vbus)
- wiegand -> [Wiegand Reader](https://esphome.io/components/wiegand)
- kuntze -> [Kuntze pool sensor](https://esphome.io/components/sensor/kuntze)
- growatt -> [Growatt Solar](https://esphome.io/components/sensor/growatt_solar)
