using System.Windows.Input;
using System.Windows;


namespace CommandExample
{
    public class MainViewModel
    {
        public ICommand ButtonCommand { get; }

        public MainViewModel()
        {
            ButtonCommand = new RelayCommand(OnButtonClick);
        }

        private void OnButtonClick()
        {
            MessageBox.Show("Button clicked using command!");
        }
    }
}
