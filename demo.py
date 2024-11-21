import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def main():
    data = np.array([56, 22, 34, 42, 22, 67, 78, 80, 95, 100])

    model_holt = ExponentialSmoothing(data, trend='add', seasonal=None)
    fit_model_holt = model_holt.fit()
    forecast_holt = fit_model_holt.forecast(steps=5)

    model_hw = ExponentialSmoothing(data, trend='add', seasonal='add', seasonal_periods=4)

    fit_model_hw = model_hw.fit()

    forecast_hw = fit_model_hw.forecast(steps=5)
    print(forecast_holt)

    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(data, label='Actual data')
    plt.plot(np.arange(len(data), len(data) + 5), forecast_holt, label='Holt Forecast')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Holt Linear Trend Method Forecasting')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(data, label='Actual data')
    plt.plot(np.arange(len(data), len(data) + 5), forecast_hw, label='Holt-Winters Foreast')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Holt-Winters Linear Trend Method Forecasting')
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
