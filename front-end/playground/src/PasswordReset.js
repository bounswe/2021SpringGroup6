import React from "react"
import './PasswordReset.css';
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import Card from "react-bootstrap/Card"
import FormControl from "react-bootstrap/FormControl"
import Alert from "react-bootstrap/Alert"
import axios from "axios";



const baseURL = "users";




class PasswordReset extends React.Component {

    constructor() {
        super()
        this.state = {
            status: false,
            form: {}, 
            isProblematic: false
        }


        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }


    handleChange(event) {

        if (event.target.name === "username") {
            let fieldName = event.target.name;
            let fleldVal = event.target.value;
            this.setState({form: {...this.state.form, [fieldName]: fleldVal}})
            console.log(this.state.form.username)
        } else {
            console.log(event.target.checked)
            this.setState({
                [event.target.id]: event.target.checked
              });
            console.log(this.state.status)
        }
        
    }

    handleSubmit(event) {
        event.preventDefault();
        if (! this.state.form || this.state.form.username.length < 3) {
            alert('Too short username, its length must be greater than 2')
        }
        else if (this.state.status === false) {
            alert('Checkme forgotten')
        } else {
            
            
            console.log('Reached1')
            axios
            .post(baseURL, {
                email : "elif@example.com",
                password : "12fgh45y2",
                identifier : "elif",
                name : "elif",
                surname : "ball",
                location : "trabzon",
                age : 22,
                gender : "female",
                sports : [{"sport":"soccer", "skill_level":2}]
            }).then((response) => {
                if(response.status === 200 || response.status === 201) {
                    alert('Your new password has been sent to your email address')
                } else {
                    alert('This username is invalid')
                }
            }
            ).catch((error) => {
                alert('This username is invalid')
            })
            console.log('Reached2')
            
        }
    }


    render() {
        return (
            <div className='page'>
                
                <br />
                {/* From https://react-bootstrap.netlify.app/components/forms/*/}
                <Card variant="success" style={{ margin: '40px'}} className='all' >
                    <h1 className="title" style={{ fontSize: '50px'}}>Password Reset Page</h1>   
                    
                    <Form className="informationForm"onSubmit={this.handleSubmit} >
                        <Form.Group className="mb-3" controlId="username">
                            <Form.Label style={{ fontSize: '30px'}}>Username</Form.Label>
                            {/*<Form.Control placeholder="Enter Username" />*/}
                            
                            <FormControl 
                                type='text'
                                name='username' 
                                placeholder='Enter Username' 
                                defaultValue={this.state.form.username}
                                onChange={this.handleChange.bind(this)}
                            />   
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="status">
                            {/*<Form.Check type="checkbox" label="Check me out" />*/}
                            <Form.Check
                                type="checkbox" 
                                label="Check me out"
                                checked={this.state.status}
                                onChange={this.handleChange}                    
                            />
                        </Form.Group>
                        <br /><br />
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                        
                    </Form>
                </Card>
                
                    <br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br>
            </div>
        )
    }

}

export default PasswordReset







