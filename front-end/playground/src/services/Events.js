import axios from 'axios';
const localData = JSON.parse(localStorage.getItem('user'));
const token = `Token ${localData.token}`;

export const getCreatedEvents = async () => {

  return axios({
    method: 'POST',
    url: `events/searches`,
    headers: {
      Authorization: token,
    },
    data: {
        creator: localData.user_id
    }
  })
    .then(response => {
      return response.data.body
    })
    .catch(error => {
      console.log(error)
    })
}

export const getEvent = async (event_id) => {

  return axios({
    method: 'GET',
    url: `events/${event_id}`,
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
