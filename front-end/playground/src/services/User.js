import axios from 'axios';
const localData = JSON.parse(localStorage.getItem('user')) || {};
const token = `Token ${localData.token}`;



export const getUserInfo = async (user_id) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'GET',
    url: `/users/${user_id}`,
    headers: {
      Authorization: token,
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const deleteUser = async (user_id) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'DELETE',
    url: `/users/${localData.user_id}`,
    headers: {
      Authorization: token,
    }
  })
    .then(response => {
      return response
    })
    .catch(error => {
      console.log(error)
    })
}


export const getNotifications = async () => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'GET',
    url: `/notifications`,
    headers: {
      Authorization: token,
    }
  })
      .then(response => {
        return response.data
      })
      .catch(error => {
        console.log(error)
      })
}


export const getOneUserInfo = async (user_id) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'GET',
    url: `/users/${user_id}`,
    headers: {
      Authorization: token,
    }
  })
    .then(response => {
      return response
    })
    .catch(error => {
      return error
      console.log(error)
    })
}

export const getUserInteresteds = async () => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'GET',
    url: `/users/${localData.user_id}/interested`,
    headers: {
      Authorization: token,
    },
    data: {
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const getUserAccepteds = async () => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'GET',
    url: `/users/${localData.user_id}/participating`,
    headers: {
      Authorization: token,
    },
    data: {
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const getUserSpectatings = async () => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'GET',
    url: `/users/${localData.user_id}/spectating`,
    headers: {
      Authorization: token,
    },
    data: {
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const getUserBadges = async () => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'GET',
    url: `/users/${localData.user_id}/badges`,
    headers: {
      Authorization: token,
    },
    data: {
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const getOtherUsersBadges = async (id) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'GET',
    url: `/users/${id}/badges`,
    headers: {
      Authorization: token,
    },
    data: {
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const changeBadgeVisibility = async (visibility) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'PUT',
    url: `/users/${localData.user_id}/visible_attributes`,
    headers: {
      Authorization: token,
    },
    data: {
      badge_visibility: visibility ? true : false
    }
  })
    .then(response => {
      return response.data.status
    })
    .catch(error => {
      console.log(error)
    })
}

export const changeCreatedEventsVisibility = async (visibility) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'PUT',
    url: `/users/${localData.user_id}/visible_attributes`,
    headers: {
      Authorization: token,
    },
    data: {
      created_events_visibility: visibility ? true : false
    }
  })
    .then(response => {
      return response.data.status
    })
    .catch(error => {
      console.log(error)
    })
}

export const getFollowings = async (user_id, param_token) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'GET',
    url: `/users/${localData.user_id || user_id}/following`,
    headers: {
      Authorization: param_token ? `Token ${param_token}` : token,
    },
    data: {
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const getFollowers = async (user_id, param_token) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'GET',
    url: `/users/${localData.user_id || user_id}/follower`,
    headers: {
      Authorization: param_token ? `Token ${param_token}` : token,
    },
    data: {
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const getBlockeds = async (user_id, param_token) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'GET',
    url: `/users/${localData.user_id || user_id}/blocked`,
    headers: {
      Authorization: param_token ? `Token ${param_token}` : token,
    },
    data: {
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const blockUser = async (user_id) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'POST',
    url: `/users/${localData.user_id}/blocked`,
    headers: {
      Authorization: token,
    },
    data: {
      user_id: user_id
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const unBlockUser = async (user_id) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'DELETE',
    url: `/users/${localData.user_id}/blocked`,
    headers: {
      Authorization: token,
    },
    data: {
      user_id: user_id
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const followUser = async (user_id) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'POST',
    url: `/users/${localData.user_id}/following`,
    headers: {
      Authorization: token,
    },
    data: {
      user_id: user_id
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}

export const unFollowUser = async (user_id) => {
  const localData = JSON.parse(localStorage.getItem('user')) || {};
  const token = `Token ${localData.token}`;

  return axios({
    method: 'DELETE',
    url: `/users/${localData.user_id}/following`,
    headers: {
      Authorization: token,
    },
    data: {
      user_id: user_id
    }
  })
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
    })
}
