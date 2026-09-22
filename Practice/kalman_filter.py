import numpy as np
class KalmanFilter:
   def __init__(self, F, H, Q, R, P, x):
       self.F = F # State transition matrix
       self.H = H # Observation matrix
       self.Q = Q # Process noise covariance
       self.R = R # Measurement noise covariance
       self.P = P # Estimate error covariance
       self.x = x # State estimate
   def predict(self):
       self.x = np.dot(self.F, self.x)
       self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q
   def update(self, z):
       y = z - np.dot(self.H, self.x)
       S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
       K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
       self.x = self.x + np.dot(K, y)
       I = np.eye(self.F.shape[1])
       self.P = np.dot(np.dot(I - np.dot(K, self.H), self.P), (I - np.dot(K, self.H)).T) + np.dot(np.dot(K, self.R), K.T)
# Example usage
F = np.array([[1, 1], [0, 1]]) # State transition matrix
H = np.array([[1, 0]]) # Observation matrix
Q = np.array([[1, 0], [0, 1]]) # Process noise covariance
R = np.array([[1]]) # Measurement noise covariance
P = np.array([[1, 0], [0, 1]]) # Estimate error covariance
x = np.array([0, 1]) # Initial state estimate
kf = KalmanFilter(F, H, Q, R, P, x)
# Predict and update steps
kf.predict()
kf.update(np.array([2]))
print(kf.x)

