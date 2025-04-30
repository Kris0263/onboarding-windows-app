## Research & Learn
###  How does WPF handle events, and what are the differences between routed events and standard events?
WPF supports both **standard .NET events** and **routed events**:

- **Standard Events**: These are typical .NET CLR events that are raised and handled on the same control. For example, `button.Click += Handler`.

- **Routed Events**: Unique to WPF, these can **travel** through the visual tree:
  - **Bubbling** (default): Event travels from the source element *up* to the root (`Button.Click` is a bubbling event).
  - **Tunneling**: Event starts from the root and goes *down* to the source (prefixed with `Preview`, like `PreviewMouseDown`).
  - **Direct**: Does not route at all—behaves like a normal .NET event.

Routed events enable parent elements to respond to child control actions, promoting modular UI design.

### What are commands in WPF, and how do they integrate with the MVVM pattern?

**Commands** encapsulate the logic for a specific action. They’re implemented using the `ICommand` interface and are crucial in **MVVM architecture** to avoid code-behind.

- In MVVM:
  - The **ViewModel** defines public properties of type `ICommand`.
  - The **View** binds UI elements (like buttons) to those command properties.
  - This decouples UI from logic and improves testability.

Built-in WPF commands (e.g., `ApplicationCommands.Copy`) exist, but custom commands are usually created using `RelayCommand` or `DelegateCommand`.

###  How does the ICommand interface facilitate the binding of commands to UI elements?

The `ICommand` interface contains:
- `Execute(object parameter)` – Defines what happens when the command is executed.
- `CanExecute(object parameter)` – Defines whether the command is currently executable.
- `CanExecuteChanged` event – Used to notify the UI to re-evaluate `CanExecute`.

## Reflection

### How does using commands improve the maintainability of your code compared to direct event handling?

Using commands:

- Removes logic from the code-behind, aligning with MVVM best practices.
- Promotes separation of concerns, making the UI (View) responsible only for presentation.
- Makes unit testing easier because the command logic lives in the ViewModel.
- Allows for command reuse across multiple controls and views.

In contrast, event handlers can make the code messy and harder to maintain in large applications.

### Reflect on scenarios where commands are more beneficial than event handlers

**Commands are ideal for:**
- Actions like Save, Submit, Delete, which need logic reuse or unit testing.
- Enabling/disabling controls dynamically with `CanExecute`.
- Multi-view applications where commands need to be shared or abstracted.

**Event handlers are more convenient for:**
- Simple UI-related tasks like animation, UI transitions, or mouse-over effects.
- One-off interactions where the ViewModel doesn’t need to be involved.

### What challenges might you encounter when implementing commands in WPF?
- Beginners may struggle with setting up `RelayCommand` or `DelegateCommand` correctly.
- If `DataContext` is not properly configured, the UI won’t find the command.
- Forgetting to raise `CanExecuteChanged` results in controls not updating their enabled/disabled states.
- Debugging command binding failures can be tricky, especially without visual errors.
