function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }


  var csrf_token = getCookie('csrftoken');

 

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
  var csrf_token = getCookie('csrftoken');
  
  
  $(document).ready(function () {
  
    $('#rzp-button').click(function (e) {
      e.preventDefault();
  
      
  
      $.ajax({
        method: 'GET',
        url: '/orders/proceed_to_pay/',
        success: function (responsedata) {
          console.log(responsedata)
  
          var options = {
            "key": "rzp_test_Oazk7hWZkgpMsZ", // Enter the Key ID generated from the Dashboard
            "amount":11 * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
            "currency": "INR",
            "name": "lenso.com",
            "description": "Thank You for Shopping with us.",
            "image": "https://example.com/your_logo",
            // "order_id": responsedata.order_id, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
            "prefill": {
              "name": responsedata.full_name,
              "email": responsedata.email,
              "contact": responsedata.mobile
            },
            "notes": {
              "address": "Razorpay Corporate Office"
            },
            "theme": {
              "color": "#3399cc"
            }
          };
          
          var rzp = new Razorpay(options);
          rzp.open();
        }
        
      });
  
  
    });
  
  
  });
  