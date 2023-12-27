// заполнение списка рецептов
function fillCourseList() {
    fetch('api/courses')
    .then(function(data) {
        return data.json();
    })

    .then(function(courses) {
        let  tbody = document.getElementById('course-list');
        tbody.innerHTML = '';
        for(let i = 0; i < courses.length; i++) {
            tr = document.createElement('tr');
            let tdName = document.createElement('td');
            tdName.innerText = courses[i].name;
            let tdVideos = document.createElement('td');
            tdVideos.innerText = courses[i].videos;
            let tdPrice = document.createElement('td');
            tdPrice.innerText = courses[i].price || 'бесплатно'; 
            
            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';
            editButton.onclick = function () {
                editCourse(i, courses[i]);
            };
            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';
            delButton.onclick = function() {
                deleteCourse(i);
            };

            let tdActions = document.createElement('td');
            tdActions.append(editButton);
            tdActions.append(delButton);

            tr.append(tdName);
            tr.append(tdVideos);
            tr.append(tdPrice);
            tr.append(tdActions);

            tbody.append(tr);
        }
    })
};


// функция удаления рецепта
function deleteCourse(num) {
    if (!confirm('Вы точно хотите удалить рецепт?')) return;
    fetch(`/api/courses/${num}`, { method: 'DELETE' })
    .then(response => {
        if (response.status === 204) {
            fillCourseList();
        } else {
            console.error('Ошибка удаления рецепта');
        }
    })
    .catch(error => {
        console.error('Ошибка удаления рецепта:', error);
    });
}
// 
function showmodal(num) {
    document.querySelector(div.modal).style.display = 'block';
};

function hidemodal(num) {
    document.querySelector(div.modal).style.display = 'none';
};

function cancel(num) {
    hidemodal();
};

function addCourse(num) {
    showmodalmodal();
};
// функция добавления курса
function addCourse() {
    document.getElementById('name').value = '';
    document.getElementById('videos').value = '';
    document.getElementById('price').value = '';
    showModal(); 
}

function sendCourse() {
    const course = {
    name: document .getElementById('name').value,
    videos: document.getElementById('videos').value,
    price: document.getElementByld('price').value,
    photo: document.getElementByld('photo').value
}}

// функция отправки рецета
function sendCourse() {
    var newCourse = {
        name: document.getElementById('name').value,
        videos: document.getElementById('videos').value,
        price: document.getElementById('price').value
    };
    
    fetch('/lab8/api/courses/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newCourse)
    })
    .then(response => response.json())
    .then(data => {
        fillCourseList();
        hideModal();
    })
    .catch(error => {
        console.error('Ошибка добавления рецепта:', error);
    });
}
function sendCourse() {
    var newCourse = {
        name: document.getElementById('name').value,
        videos: document.getElementById('videos').value,
        price: document.getElementById('price').value,
        photo: document.getElementById('photo').value
    };

    fetch('/lab8/api/courses/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newCourse)
    })
    .then(response => {
        if (response.status === 201) {
            fillCourseList();
            hideModal();
        } else {
            console.error('Ошибка добавления рецепта');
        }
    })
    .catch(error => {
        console.error('Ошибка добавления рецепта:', error);
    });
}


window.addEventListener('scroll', function() {
    var scrollButton = document.getElementById('scroll-to-bottom');
    if (window.pageYOffset > 0) {
      scrollButton.style.display = 'block';
    } else {
      scrollButton.style.display = 'none';
    }
  });
  
  document.getElementById('scroll-to-bottom').addEventListener('click', function() {
    document.documentElement.scrollTop = document.documentElement.scrollHeight;
  });


  function editCourse(courseIndex) {
    const course = courses[courseIndex];
}


function deleteCourse(courseIndex) {
    fetch('api/courses/' + num, { method: 'DELETE' })
    .then(response => {
        if (response.status === 204) {
            fillCourseList();
        }
    })
    .catch(error => {
        console.error('Ошибка удаления рецепта:', error);
    });
}