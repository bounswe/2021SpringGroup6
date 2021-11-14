// ** Router Import
import Router from './router/Router'

import { Fragment, useEffect, useContext, useState } from 'react'
import { toast } from 'react-toastify'
import Avatar from '@components/avatar'
import { Bell } from 'react-feather'
import { getFirebaseMessaging } from './firebase'

import { NotificationContext } from './utility/context/notificationContext'
import { getUnseenCount } from './services/NotificationService'

// ** Toast Component
const ToastComponent = ({ title, icon, color, body }) => (
  <Fragment>
    <div className='toastify-header pb-0'>
      <div className='title-wrapper'>
        <Avatar size='sm' color={color} icon={icon} />
        <h6 className='toast-title'>{title}</h6>
      </div>
    </div>
    <div className='toastify-body'>
      <span role='img' aria-label='toast-text'>
        {body}
      </span>
    </div>
  </Fragment>
)

const App = props => {
  const [state, dispatch] = useContext(NotificationContext)

  const onMessageListener = () => {
    new Promise(_ => {
      try {
        getFirebaseMessaging().onMessage(payload => {
          // resolve(payload)
          const notification = payload.notification

          dispatch({ type: 'increase_unread' })

          toast.success(
            <ToastComponent title={notification.title} body={notification.body} color='success' icon={<Bell />} />,
            {
              hideProgressBar: true,
              closeButton: true
            }
          )
        })
      } catch (exception) {}
    })
  }

  useEffect(() => {
    getUnseenCount().then(response => {
      dispatch({ type: 'set_count', newCount: response })
    })
    onMessageListener()
  }, [])

  return <Router />
}

export default App
