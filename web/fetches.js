
const origin = window.location.origin

async function getDefectById(id){
    const response  = await  fetch(`${origin}/defects/${id}`)
    const defect = await response.json()
    return defect
}


async function updateStatus(id, status = ""){

    const options = {
        method:"PATCH", 
        body:JSON.stringify({status}), 
        headers:{
            "Content-Type":"application/json"
        }};

    const response  = await  fetch(`${origin}/defects/${id}`,options)
    return response
}