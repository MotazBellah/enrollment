const title = React.createElement(
    'h1',
    {id: 'main-title', title: 'This a title.'},
    'My First React Element!'
);

const desc = React.createElement(
    'p',
    null,
    "I just learned how to create a React node :)"
);

const header = React.createElement(
    'header',
    null,
    title, desc
);

ReactDOM.render(
    header,
    document.getElementById('root')
);

// class Hello extends React.Component {
//   render() {
//     return <div>Hello {this.props.foo}. This is a {this.props.test}</div>;
//   }
// }
//
// ReactDOM.render(
//   <Hello {...(root.dataset)}/>,
//   document.getElementById('root')
);
