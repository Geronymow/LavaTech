function add_car() {

    let container = document.getElementById("form-car");

    let html = `
        <br> 
        <div class='row'> 
            <div class='col-md'> 
                <input type='text' placeholder='car' class='form-control' name='car'> 
            </div> 
            <div class='col-md'> 
                <input type='text' placeholder='plate' class='form-control' name='plate'> 
            </div> 
            <div class='col-md'> 
                <input type='number' placeholder='year' class='form-control' name='year'> 
            </div> 
        </div>
    `;

    container.innerHTML += html;
}

function display_form(type){

    add_customer = document.getElementById('add-customers')
    upp_customer = document.getElementById('upp_customer')

    if(type == "1"){
        upp_customer.style.display = "none"
        add_customer.style.display = "block"
    } 
    else if(type == "2") {
        add_customer.style.display = "none"
        upp_customer.style.display = "block"
    }
}

function customer_data(){
    customer = document.getElementById('customer-select')

    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    console.log(csrf_token)
    id_customer = customer.value

    data = new FormData()
    data.append('id_customer', id_customer)

    fetch("/customers/update_customer/",{
        method: "POST",
        headers:{
            'X-CSRFToken': csrf_token
        },
        body: data

    }).then(function(result){
        return result.json()

    }).then(function(data){

        document.getElementById('form-upp-customer').style.display = 'block'

        dataname = document.getElementById('firstname')
        dataname.value = data['firstname']

        datalastname = document.getElementById('lastname')
        datalastname.value = data['lastname']

        dataemail = document.getElementById('email')
        dataemail.value = data['email']

        datacpf = document.getElementById('cpf')
        datacpf.value = data['cpf']

    })

}