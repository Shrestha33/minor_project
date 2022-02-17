import { authActions } from "./auth-slice";

export const authMiddleware = (store) => (next) => (action) => {
  if (authActions.loginSuccess.match(action)) {
    localStorage.setItem("access", action.payload.access);
    localStorage.setItem("refresh", action.payload.refresh);
  } else if (
    authActions.logOut.match(action) ||
    authActions.loginFail.match(action)
  ) {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
  }
  return next(action);
};
