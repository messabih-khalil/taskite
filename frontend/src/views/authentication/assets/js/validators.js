const regex = {
  username: /^[a-z0-9_\.]+$/i,
  email: /^[\w\d._-]+@(?:[\w\d-]+\.)+(\w{2,})$/i,
  password: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/,
};

export function validate(pattern, value) {
  if (pattern != 'repeatPassword') {
    return regex[pattern].test(value);
  }
}

export function isEmpty(value) {
  if (value == '') {
    return true;
  }
}

// Validate Password
export class ValidationActions {
  constructor(userInfo) {
    this.validated = false;
    this.userInfo = userInfo;
  }
  // Validate All Inputs
  validateInputs() {
    
    // Validate Inputs
    let inputs = document.querySelectorAll('input');
    inputs.forEach((el) => {
      el.addEventListener('keyup', (e) => {
        let input = document.querySelector(
          `input[name=${e.target.attributes.name.value}]`
        );
        if (!!validate(e.target.attributes.name.value, e.target.value)) {
          input.classList.remove('err-border');
          this.validated = true;
        } else {
          input.classList.add('err-border');
          this.validated = false;
        }
      });
    });

    
  }
  validatePassword() {
    // Verify Password inputs if they match
    let password2 = document.querySelector('input[name="repeatPassword"]');
    password2.addEventListener('keyup', (e) => {
      if (
        e.target.value === this.userInfo.password &&
        (e.target.value != '' || this.userInfo.password != '')
      ) {
        password2.classList.remove('err-border');
        this.validated = true;
      } else {
        password2.classList.add('err-border');
        this.validated = false;
      }
    });
  }

  // Validate Empty input
  validateEmpty() {
    for (let val in this.userInfo) {
      if (isEmpty(this.userInfo[val])) {
        let input = document.querySelector(`input[name=${val}]`);
        input.classList.add('err-border');
        this.validated = false;
      } else {
        this.validated = true;
      }
    }
  }

  getValidation() {
    return this.validated;
  }
}
