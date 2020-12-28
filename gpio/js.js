export default class EdgeGPIOUtils {
  /*
  used for scaling a UO !!! YES its backwards 0 is high and 100 is low !!!
  to drive a UO as an DO send 0 for ON and 100 for OFF // Example to send 6vdc console.log(scaleToGPIOValue(60, 0, 120)) returns 48
  to drive a UO as an AO send 100 to 0 as a float
  */
  static scaleToGPIOValue = (
    val: number,
    minOutput: number,
    maxOutput: number,
    minInput = 120,
    maxInput = 0,
  ): number => {
    let value = val;
    let pinValue = ((maxOutput - minOutput) * (value - minInput)) / (maxInput - minInput) + minOutput;
    if (pinValue > maxOutput) {
      pinValue = maxOutput;
      value = maxInput;
    } else if (pinValue < minOutput) {
      pinValue = minOutput;
      value = minInput;
    }
    return pinValue;
  };

  /*
    used for scaling a UI
    Example for scaling a 0/10dc to 0 to 1000.
    scaleFromGPIOValue(0.7, 0, 1000)
    */
  static scaleFromGPIOValue = (
    pinValue: number,
    minOutput: number,
    maxOutput: number,
    minInput = 0,
    maxInput = 1,
  ): number => {
    return ((maxOutput - minOutput) * (pinValue - minInput)) / (maxInput - minInput) + minOutput;
  };

  /*
    used for scaling a UI as a DI
    off/open = around 0.9 vdc. When on the pin jumper its set as a 10K
    on/closed = around 0.1 vdc
    */
  static uiAsDI = (val: number): number => {
    if (val > 0.6) {
      return 0; // false/open
    }
    if (val < 0.2) {
      return 1; // true/closed
    }
  };

  /*
    The bbb returns the DI as 0 for closed/on and 1 for open/off
  */
  static diInvert = (val: number): number => {
    return (val ^= 1);
  };

  //  scale or convert 4-20mA reading to temperature
  //      -value_420 is input value in 4-20mA
  //      -min_target is minimum target temperature @4mA, defualts to 0C
  //      -max_target is maximum target temperature  @20mA, defualts to 100C
  //      -min_range is minimum input range, defaults to 4 mA.
  //      -max_range is maximum input range, defaults to 20mA

  static scale420maToRange(value_420: number, min_target: number, max_target: number) {
    const limit = true,
      min_range = 4,
      max_range = 20;
    const slope = (max_target - min_target) / (max_range - min_range);
    if (limit)
      if (value_420 <= min_range) return min_target;
      else if (value_420 >= max_range) return max_target;
    return (value_420 - min_range) * slope + min_target;
  }

  //  scale or convert ui reading to 4-20mA
  //      -ui_value is input value in ui reading (0-1 range)
  //      -min_target is minimum target output, defualts to 4mA
  //      -max_target is maximum target output, defualts to 20mA
  //      -min_range is minimum input range, defaults to 0.0
  //      -max_range is maximum input range, defaults to 1.0
  //

  static scaleUI420ma(ui_value: number, min_range: number, max_range: number) {
    const min_target = 4,
      max_target = 20,
      limit = true;
    const slope = max_target / (max_range - min_range);
    const value_420 = (ui_value - min_range) * slope;
    if (limit)
      if (value_420 <= min_target) return min_target;
      else if (value_420 >= max_target) return max_target;

    return value_420;
  }
}

  /**
   * Values will be converted into the range min-max
   * @param {number} value
   * @param {number} min
   * @param {number} max
   */
  static clamp(value: number, min: number, max: number): number {
    return Math.min(Math.max(value, min), max);
  }
