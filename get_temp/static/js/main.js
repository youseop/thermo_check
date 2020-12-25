init();

function init() {
    scrollEvent();
}

function submit_thermo() {
    const num_sub = document.getElementById("num_sub");
    const num_main = document.getElementById("num_main");
    const input_thermo = document.getElementById("thermo_input");
    const form_thermo = document.getElementById("form_thermo");
    let result = num_main.innerText + "." + num_sub.innerText;
    input_thermo.value = result
    form_thermo.submit()
}


function scrollEvent() {
    const num_sub = document.getElementById("num_sub");
    const num_main = document.getElementById("num_main");
    const wrapper = document.getElementById("wrapper");
    let startY;
    let endY;
    let check_element;

    num_sub.addEventListener("touchstart", function (e) {
        startY = e.changedTouches[0].screenY;
        check_element = num_sub
    });

    num_main.addEventListener("touchstart", function (e) {
        startY = e.changedTouches[0].screenY;
        check_element = num_main
    });

    wrapper.addEventListener("touchend", function (e) {
        endY = e.changedTouches[0].screenY;
        let tmp_value;
        if (startY != null) {
            if (endY > startY) {
                tmp_value = check_element.innerText;
                limitDegree(false, tmp_value, check_element, num_main, num_sub)
                check_element = null
                startY = null
            } else {
                tmp_value = check_element.innerText;
                limitDegree(true, tmp_value, check_element, num_main, num_sub)
                startY = null
                check_element = null
            }
        }
    });
}

function limitDegree(direction, value, element, main, sub) {

    if (element === main) {
        if (direction) {
            if (value < 36) {
                alert('체온이 너무 낮습니다.')
            } else {
                let change_num = String(parseInt(value) - 1);
                element.innerHTML = change_num
            }
        } else {
            if (value > 37) {
                alert('체온이 너무 높습니다.')
            } else {
                let change_num = String(parseInt(value) + 1);
                element.innerHTML = change_num
            }
        }
    } else if (element === sub) {
        if (direction) {
            let change_num;
            if (value < 1) {
                change_num = 9
            } else {
                change_num = String(parseInt(value) - 1);
            }
            element.innerHTML = change_num

        } else {
            let change_num;
            if (value > 8) {
                change_num = 0
            } else {
                change_num = String(parseInt(value) + 1);
            }
            element.innerHTML = change_num
        }
    }
}
