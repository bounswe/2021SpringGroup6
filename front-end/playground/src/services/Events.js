import axios from 'axios';

const localData = JSON.parse(localStorage.getItem('user')) || {};
const token = `Token ${localData.token}`;

export const createEvent = async (event_id, text = 'text') => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'POST',
        url: `/events/${event_id}/discussion`,
        headers: {
            Authorization: token,
        },
        data: {
            text,
        }
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}
export const getEvents = async (eventId) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'GET',
        url: `/events/${eventId}/discussion`,
        headers: {
            Authorization: token,
        },
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}

export const getCreatedEvents = async () => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'POST',
        url: `/events/searches`,
        headers: {
            Authorization: token,
        },
        data: {
            creator: localData.user_id
        }
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}

export const getOtherUsersCreatedEvents = async (user_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'POST',
        url: `/events/searches`,
        headers: {
            Authorization: token,
        },
        data: {
            creator: user_id
        }
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}

export const getEvent = async (event_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'GET',
        url: `/events/${event_id}`,
        headers: {
            Authorization: token,
        },
        data: {}
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}

export const deleteEvent = async (event_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'DELETE',
        url: `/events/${event_id}`,
        headers: {
            Authorization: token,
        },
        data: {}
    })
        .then(response => {
            return response
        })
        .catch(error => {
            console.log(error)
        })
}

export const getEventParticipants = async (event_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'GET',
        url: `/events/${event_id}/participants`,
        headers: {
            Authorization: token,
        },
        data: {}
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}

export const getEventInteresteds = async (event_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'GET',
        url: `/events/${event_id}/interesteds`,
        headers: {
            Authorization: token,
        },
        data: {}
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}

export const postSpectatorDecleration = async (event_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'POST',
        url: `/events/${event_id}/spectators`,
        headers: {
            Authorization: token,
        },
        data: {}
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}

export const undoSpectatorDecleration = async (event_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'DELETE',
        url: `/events/${event_id}/spectators`,
        headers: {
            Authorization: token,
        },
        data: {}
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}

export const postParticipationRequest = async (event_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'POST',
        url: `/events/${event_id}/interesteds`,
        headers: {
            Authorization: token,
        },
        data: {}
    })
        .then(response => {
            return response
        })
        .catch(error => {
            console.log(error)
        })
}

export const undoParticipation = async (event_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'DELETE',
        url: `/events/${event_id}/participants`,
        headers: {
            Authorization: token,
        },
        data: {}
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}

export const undoInterest = async (event_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'DELETE',
        url: `/events/${event_id}/interesteds`,
        headers: {
            Authorization: token,
        },
        data: {}
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}

export const acceptInterested = async (event_id, user_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'POST',
        url: `/events/${event_id}/participants`,
        headers: {
            Authorization: token,
        },
        data: {
            accept_user_id_list: [user_id],
            reject_user_id_list: []
        }
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}

export const rejectInterested = async (event_id, user_id) => {
    const localData = JSON.parse(localStorage.getItem('user')) || {};
    const token = `Token ${localData.token}`;

    return axios({
        method: 'POST',
        url: `/events/${event_id}/participants`,
        headers: {
            Authorization: token,
        },
        data: {
            accept_user_id_list: [],
            reject_user_id_list: [user_id]
        }
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}
