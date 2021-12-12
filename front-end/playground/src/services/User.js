import axios from 'axios';
const localData = JSON.parse(localStorage.getItem('user'));
const token = `Token ${localData.token}`;

export const getUserInfo = async (user_id) => {
    console.log('token\n', token)
  return axios({
    method: 'GET',
    url: `/users/${user_id}`,
    headers: {
      Authorization: token,
    }
  })
    .then(response => {
      return response.data.body
    })
    .catch(error => {
      console.log(error)
    })
}

export const getUserInteresteds = async () => {

  return axios({
    method: 'GET',
    url: `users/${localData.user_id}/interested`,
    headers: {
      Authorization: token,
    },
    data: {
    }
  })
    .then(response => {
      return response.data.body
    })
    .catch(error => {
      console.log(error)
    })
}

export const getUserAccepteds = async () => {

  return axios({
    method: 'GET',
    url: `users/${localData.user_id}/participating`,
    headers: {
      Authorization: token,
    },
    data: {
    }
  })
    .then(response => {
      return response.data.body
    })
    .catch(error => {
      console.log(error)
    })
}

export const getUserSpectatings = async () => {

  return axios({
    method: 'GET',
    url: `users/${localData.user_id}/spectating`,
    headers: {
      Authorization: token,
    },
    data: {
    }
  })
    .then(response => {
      return response.data.body
    })
    .catch(error => {
      console.log(error)
    })
}
