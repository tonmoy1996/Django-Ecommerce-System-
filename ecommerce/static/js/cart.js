var updatebtn = document.getElementsByClassName('update-cart');
for (var i = 0; i < updatebtn.length; i++) {
  updatebtn[i].addEventListener('click', function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log('Product id:', productId, 'action', action);

    if (user == 'AnonymousUser') {
      console.log('User is not logged in..');
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function updateUserOrder(productId, action) {
  var url = '/update_item/';
  console.log('sasasas');
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log('data', data);
      location.reload();
    });
}
