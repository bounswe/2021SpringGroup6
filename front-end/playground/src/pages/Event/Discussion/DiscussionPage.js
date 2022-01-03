import {React, useState, Fragment, useEffect} from 'react';
import {useNavigate, useParams} from "react-router-dom";
import {createEvent, getEvents} from "../../../services/Events";

function DiscussionPage(props) {

    const {eventInfo, isLoading} = props;
    const [comment, setComment] = useState("");
    const [comments, setComments] = useState([]);

    useEffect(() => {
        getDiscussions()
    }, [eventInfo])


    const getDiscussions = () => {
        getEvents(eventInfo.event_id).then((response) => {
            console.log('comments', response.additionalProperty.value)

            if (response.additionalProperty && response.additionalProperty.value) {
                setComments(response.additionalProperty.value)
            }
        })
    }

    const handleStore = (e) => {
        e.preventDefault();
        if (!comment)
            return false;


        createEvent(eventInfo.event_id, comment).then((response) => {
            setComment('')
            getDiscussions();
        })
    }


    return (
        <>
            <h3 className="m-5">Comments</h3>

            {
                comments.map((comment, i) => {
                    console.log(comment)
                    return (
                        <div key={comment['@id']} className="d-flex flex-row">
                            <label htmlFor="">{i} -  </label>
                            <p> {comment.author['@id']} / </p>
                            <p>{comment.text} - </p>
                        </div>
                    )
                })
            }


            <form>
                <label>Type your comment here:</label>
                <textarea
                    className={'col-lg-12'}
                    value={comment}
                    onChange={(e) => setComment(e.target.value)}
                />

                <button onClick={handleStore} className={'btn btn-success col-lg-12'}>
                    STORE
                </button>
            </form>
        </>
    )
}

export {DiscussionPage};
